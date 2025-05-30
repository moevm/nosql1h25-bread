from djongo import models
from django.contrib.auth.models import AbstractUser


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
    )  # Делаем email уникальным
    first_name = models.CharField("Имя", max_length=30, blank=False)
    last_name = models.CharField("Фамилия", max_length=150, blank=False)
    update_at = models.DateTimeField(auto_now=True)
    comments = models.ArrayField(model_container=IntItem, default=list)

    # class Meta:
    #     db_table = "User"
