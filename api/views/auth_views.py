from datetime import datetime
import logging
from api.serializers.auth_serializers import ChangePasswordSerializer, CreateUserSerializer, CustomTokenObtainPairSerializer, GroupSerializer, SetPasswordSerializer, UserSerializer
from api.services.auth_service import AuthService
import logging
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password,check_password
from api.models.auth_models import User




logger = logging.getLogger(__name__)



class ObtainTokenPairAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserApiView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    service = AuthService

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            phone = serializer.validated_data["phone"]
            email = serializer.validated_data["email"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]
            password = serializer.validated_data["password"]

            hashed_password = make_password(password)

        
            user = self.service.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=hashed_password,
            )
            user.password = hashed_password
            user.save()
            user.groups.add("TestGroup")

            self.serializer_class = UserSerializer
            resp = self.serializer_class(user)
            
            return Response(resp.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
          

class SetInitialPasswordApiView(generics.CreateAPIView):
    serializer_class = SetPasswordSerializer
    service = AuthService

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            print(kwargs["id"])
            self.service.save_password(kwargs["id"], serializer.validated_data["password"])
            return Response({"message":"password reset successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error("Password reset failed: %s", e)
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetApiView(generics.CreateAPIView):
    serializer_class = ChangePasswordSerializer
    service = AuthService

    def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get("email", None)
            new_password=serializer.validated_data.get("new_password", None)
            
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                    return Response({"message": f"No active user with email {email} found"}, status=status.HTTP_400_BAD_REQUEST)
                
                
            initial_password=user.password
            
            if check_password(new_password, initial_password):
                return Response({"message": "Initial Password cannot be the same as the new password,please try again with a new password!"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_password = make_password(new_password)
            user.password=new_password
            user.save()
            return Response({"message":"User password successfully updated"},status=status.HTTP_200_OK)

class ListUsersAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = AuthService.list_users()
    permission_classes = (IsAuthenticated, )

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['groups__name']
    ordering_fields = [ 'groups__name']

    def get_queryset(self):
        return self.queryset
    

class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = AuthService.list_users()
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.method == 'GET':
            self.serializer_class = UserSerializer
        return self.queryset.filter()


class GroupApiView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = AuthService.list_groups()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(Group, id=self.request.query_params.get('id'))

    def get_queryset(self):
        return self.queryset
