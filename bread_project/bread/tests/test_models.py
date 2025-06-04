from django.test import TestCase
from ..models import IntItem, Recipe
from django.core.exceptions import ValidationError

class IntItemTest(TestCase):
    def test_int_item_creation(self):
        item = IntItem(value=42)
        self.assertEqual(item.value, 42)  # Проверка значения
        self.assertTrue(item._meta.abstract)  # Проверка, что модель абстрактная


class RecipeTest(TestCase):
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            RecipeID="r1",
            Title="Бородинский хлеб",
            Composition="Мука, вода, солод",
            Recipe="Вымесить тесто...",
            Rate=4.5,
            Image="bread.jpg",
            CommentIDs=[{"value": 1}, {"value": 2}]  # Пример для ArrayField
        )
        self.assertEqual(recipe.Title, "Бородинский хлеб")
        self.assertEqual(recipe.CommentIDs[0]["value"], 1)  # Проверка CommentIDs


class RecipeValidationTest(TestCase):
    def test_required_fields(self):
        recipe = Recipe(
            Rate=5.0,
            CommentIDs=[]
        )
        with self.assertRaises(ValidationError):  # Ожидаем ошибку валидации
            recipe.full_clean()  # Проверяет все поля модели


class RecipeArrayFieldTest(TestCase):
    def test_comment_ids_saving(self):
        recipe = Recipe.objects.create(
            RecipeID="r2",
            Title="Ржаной хлеб",
            CommentIDs=[{"value": 10}, {"value": 20}]
        )
        saved_recipe = Recipe.objects.get(RecipeID="r2")
        self.assertEqual(len(saved_recipe.CommentIDs), 2)
        self.assertEqual(saved_recipe.CommentIDs[1]["value"], 20)
