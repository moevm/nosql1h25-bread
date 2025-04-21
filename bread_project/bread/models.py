from djongo import models

# Create your models here.

class IntItem(models.Model):
    value = models.IntegerField()

    class Meta:
        abstract = True


class Recipe(models.Model):
    RecipeID   = models.CharField(primary_key=True, max_length=50)
    Title      = models.CharField(max_length=200)
    Composition= models.TextField()
    Date       = models.DateTimeField(auto_now_add=True)
    Recipe     = models.TextField()
    Rate       = models.IntegerField()
    CommentIDs = models.ArrayField(
        model_container=IntItem,
        default=list
                 )

    class Meta:
        db_table = 'Recipe'


