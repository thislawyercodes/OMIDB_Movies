from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.contrib.auth.models import Group

User = get_user_model()


class AuthService:

    @staticmethod
    def list_users():
        return User.objects.all()

    @staticmethod
    def filter_user(filter_params: dict) -> QuerySet[User]:
        return User.objects.filter(**filter_params)

    @staticmethod
    def save_password(user_id, password: str):
        return User.objects.set_initial_password(
                    id=user_id,
                    password=password)

    @staticmethod
    def delete_user(user_id):
        return User.objects.filter(pk=user_id).soft_delete()

    @staticmethod
    def activate_user(user_id: str):
        try:
            return User.objects.filter(pk=user_id).update(is_active=True)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(email: str,first_name: str, last_name: str,
                    phone:str,password:str,) -> User:
        user = User.objects.create_user(email=email,first_name=first_name,
                                         last_name=last_name,phone=phone,password=password
                                       )
        
        return user
    
    @staticmethod
    def list_groups() -> QuerySet[Group]:
        return Group.objects.all()
