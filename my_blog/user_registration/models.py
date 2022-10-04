
from django.db import models
from django.contrib.auth.models import User

class ProfilModel(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-jpg', upload_to="profile_pics")

    class Meta:
        db_table = "profile"

    def __str__(self):
        return f"{self.user.username} Profile"