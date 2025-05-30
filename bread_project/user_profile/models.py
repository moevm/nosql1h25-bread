from djongo import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class IntItem(models.Model):
    value = models.IntegerField()

    class Meta:
        abstract = True


class MyUser(AbstractUser):
    username = models.CharField("Никнейм", max_length=30, blank=False, unique=True)
    email = models.EmailField(
        "Email",
        blank=False,
        unique=True,
        max_length=254,
    )
    first_name = models.CharField("Имя", max_length=30, blank=False)
    last_name = models.CharField("Фамилия", max_length=150, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    comments = models.ArrayField(model_container=IntItem, default=list)
