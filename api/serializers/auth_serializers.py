from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()




class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
                                      

class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)



class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
             

        data['username'] = self.user.username
        data['groups'] = self.user.groups.values_list('name', flat=True)
        data['id'] = self.user.id
        data['is_superuser'] = self.user.is_superuser
        data['is_staff'] = self.user.is_staff
        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['phone'] = str(self.user.phone)
    

        return data
