from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=50,unique = True)
    email = models.EmailField("Email", unique=True)
    image = models.ImageField(upload_to = "account/", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "{}".format(self.username)