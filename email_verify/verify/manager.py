from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The mail must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('superuser must have is_superuser=True'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('superuser must have is_superuser=True'))
        return self._create_user(email, password, **extra_fields)