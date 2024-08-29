from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('This Email Field Must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    
# General Information
# class GeneralInfo(models.Model):
#     company_logo = models.ImageField(upload_to="logo/")
#     company_image = models.CharField(max_length=225, blank=True, null=True, default="Add")
#     director = models.CharField(max_length=60, blank=True, null=True)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     # socials 
#     fb_link = models.URLField(blank=True, null=True)
#     ig_link = models.URLField(blank=True, null=True)
#     x_link = models.URLField(blank=True, null=True)
#     pin_link = models.URLField(blank=True, null=True)
#     yb_link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.director
    

# # Hero - section model 
# class HeroCarousel(models.Model):
#     theme = models.CharField(max_length=255, null=True, blank=True)
#     description = models.CharField(max_length=255, null=True, blank=True)
#     bg_image = models.ImageField(upload_to='hero_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.theme

# # Hero - section model 
# class ViewMore(models.Model):
#     theme = models.CharField(max_length=255, null=True, blank=True)
#     bg_image = models.ImageField(upload_to='view_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.theme



# class Gallery(models.Model):
#     event_name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='gallery/', null=True, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.event_name


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     country = models.CharField(max_length=50)
#     joined_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.first_name


# class Blog(models.Model):
#     image = models.ImageField(upload_to ='blogs/')
#     category = models.CharField(max_length=50, null=True, blank=True)
#     title = models.CharField(max_length=100, blank=True)
#     description = models.CharField(max_length=100, default="Enter value", blank=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
#     content = models.TextField(blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class UpcomingEvent(models.Model):
#     title = models.CharField(max_length=100, blank=False)
#     image = models.ImageField(upload_to ='Upcoming_event/')
    
#     def __str__(self):
#         return self.title
