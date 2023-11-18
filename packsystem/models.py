from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PackageSystemUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
