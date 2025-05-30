from djongo import models
from django.contrib.auth.models import AbstractUser



class IntItem(models.Model):
    value = models.IntegerField()

    class Meta:
        abstract=True

class Recipe(models.Model):
    RecipeID   = models.CharField(primary_key=True, max_length=50)
    Title      = models.CharField(max_length=200)
    Composition= models.TextField()
    Date       = models.DateTimeField(auto_now_add=True)
    Recipe     = models.TextField()
    Rate       = models.FloatField()
    Image      = models.CharField(max_length=200)
    CommentIDs = models.ArrayField(
        model_container=IntItem,
        default=list
                 )



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
