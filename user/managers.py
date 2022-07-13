from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def normalize_phone(self, primary_phone):
        return primary_phone
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, primary_phone, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not primary_phone:
            raise ValueError('The phone must be set')
        primary_phone = self.normalize_phone(primary_phone)
        user = self.model(primary_phone=primary_phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, primary_phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(primary_phone, password, **extra_fields)