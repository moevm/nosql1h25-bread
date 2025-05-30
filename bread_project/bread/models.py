from djongo import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Recipe(models.Model):
    RecipeID = models.CharField(primary_key=True, max_length=50)
    Title = models.CharField(max_length=200)
    Composition = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Recipe = models.TextField()
    Rate = models.IntegerField()


# class IntItem(models.Model):
#     value = models.IntegerField()
#
#
# class Recipe(models.Model):
#     RecipeID = models.CharField(primary_key=True, max_length=50)
#     Title = models.CharField(max_length=200)
#     Composition = models.TextField()
#     Date = models.DateTimeField(auto_now_add=True)
#     Recipe = models.TextField()
#     Rate = models.IntegerField()
#     CommentIDs = models.ArrayField(model_container=IntItem, default=list)
#
#     class Meta:
#         db_table = "Recipe"
#
#
# class User(models.Model):
#     UserID = models.CharField(primary_key=True, max_length=50)
#     Name = models.CharField(max_length=100)
#     Surname = models.CharField(max_length=100)
#     Nickname = models.CharField(max_length=100)
#     Create_Date = models.DateTimeField(auto_now_add=True)
#     Last_Redact_Date = models.DateTimeField(auto_now=True)
#     email = models.EmailField(unique=True)
#     CommentIDs = models.ArrayField(model_container=IntItem, default=list)
#     hash_Password = models.CharField(max_length=255)
#     class Meta:
#         db_table = "User"


#
#
# class Comment(models.Model):
#     CommentID = models.CharField(primary_key=True, max_length=50)
#     Username = models.CharField(max_length=100)
#     Text = models.TextField()
#     Rating = models.IntegerField()
#     Date = models.DateTimeField(auto_now_add=True)
#     RecipeID = models.CharField(max_length=50)
#     Title = models.CharField(max_length=200)
#
#     class Meta:
#         db_table = "Comment"
