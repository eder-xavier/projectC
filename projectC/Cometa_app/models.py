from django.db import models
from Titan_app.models import CustomUserTitan
# Create your models here.

class UserProfileCometa(models.Model):
    user = models.OneToOneField(CustomUserTitan, on_delete=models.CASCADE, related_name='user_cometa')
    profile_picture = models.ImageField(upload_to='profile_pictures/',  blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, )

    def __str__(self):
        return self.user.username