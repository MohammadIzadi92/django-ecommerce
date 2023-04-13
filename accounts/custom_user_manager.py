from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, birthday, sex, password=None, **other_fields):
        if not phone_number:
            raise ValueError("Phone number is required ... !")
        if not first_name:
            raise ValueError("First name is required ... !")
        if not last_name:
            raise ValueError("Last name is required ... !")
        if not birthday:
            raise ValueError("Birthday is required ... !")
        if not sex:
            raise ValueError("Sex is required ... !")
        
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, birthday=birthday, sex=sex, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone_number, first_name, last_name, birthday, sex, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(phone_number, first_name, last_name, birthday, sex, password, **other_fields)
