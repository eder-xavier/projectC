# models.py
#from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
#from django.db import models
#from django.utils import timezone
#from django.contrib.auth.hashers import make_password, check_password
#    
#
#class CustomUserTitan(AbstractUser):
#
#    username = models.CharField(max_length=30, unique=True)
#    name = models.CharField(max_length=100)
#    email = models.EmailField()
#    registration_code = models.CharField(max_length=20, blank=True, null=True)
#    
#    # Adicionando related_name para evitar colisões
#    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set', related_query_name='user')
#    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set', related_query_name='user')
#
#    def save(self, *args, **kwargs):
#        if not self.pk:
#            super().save(*args, **kwargs)
#
#
#    def check_password(self, raw_password):
#        return check_password(raw_password, self.password)
#
#    def __str__(self):
#        return self.username
#    
#
#class UserProfileTitan(models.Model):
#    user = models.OneToOneField(CustomUserTitan, on_delete=models.CASCADE, related_name='profile')
#    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#    bio = models.TextField(max_length=300, blank=True)
#
#    def __str__(self): 
#        return self.user.username
#    
#class News(models.Model):
#    user = models.ForeignKey(CustomUserTitan, on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    media = models.ImageField(upload_to='news_media/', null=True, blank=True)
#    video_url = models.URLField(null=True, blank=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return self.title
#