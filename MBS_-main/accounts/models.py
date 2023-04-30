from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField()
    address = models.TextField(default=None, null=True)
    phone_number = models.TextField(default=None, null=True)
    gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'),('FEMALE', 'FEMALE')]
    )

    def __str__(self):
        return self.user.username