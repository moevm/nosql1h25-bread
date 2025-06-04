from django.test import TestCase, Client
from django.urls import reverse
from ..models import Recipe
from datetime import datetime, timedelta

class BreadViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe1 = Recipe.objects.create(
            RecipeID="r1",
            Title="Бородинский хлеб",
            Composition="ржаная мука, солод",
            Recipe="Выпекать 40 минут",
            Rate=4.5,
            Date=datetime.now() - timedelta(days=2))
        cls.recipe2 = Recipe.objects.create(
            RecipeID="r2",
            Title="Белый батон",
            Composition="пшеничная мука",
            Recipe="Выпекать 30 минут",
            Rate=3.0,
            Date=datetime.now() - timedelta(days=1))
        cls.client = Client()

    def test_bread_list_GET(self):
        response = self.client.get(reverse('bread:bread_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bread/bread_list.html')
        self.assertContains(response, 'Бородинский хлеб')

    def test_bread_list_search_filter(self):
        response = self.client.get(reverse('bread:bread_list') + '?q=бородинский')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Бородинский хлеб')
        self.assertNotContains(response, 'Белый батон')

    def test_bread_list_date_filter(self):
        Recipe.objects.create(
            RecipeID="r3",
            Title="Свежий хлеб",
            Composition="мука",
            Recipe="...",
            Rate=4.0,
            Date=datetime.now()
        )
        date_from = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        response = self.client.get(f"{reverse('bread:bread_list')}?date-from={date_from}")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Белый батон')  # r2 (вчера)
        self.assertContains(response, 'Свежий хлеб')  # r3 (сегодня)

    def test_bread_list_rating_filter(self):
        response = self.client.get(reverse('bread:bread_list') + '?rating-filter=4')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Бородинский хлеб')
        self.assertNotContains(response, 'Белый батон')

    def test_bread_list_reset_filter(self):
        response = self.client.get(reverse('bread:bread_list') + '?reset=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Бородинский хлеб')
        self.assertContains(response, 'Белый батон')

    def test_bread_detail_404(self):
        response = self.client.get(reverse('bread:bread_detail', kwargs={'pk': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)

    def test_bread_detail_preserves_filters(self):
        response = self.client.get(
            reverse('bread:bread_detail', kwargs={'pk': 'r1'}) + '?q=хлеб&date-from=2023-01-01&rating-filter=4'
        )
        self.assertEqual(response.context['query'], 'хлеб')
        self.assertEqual(response.context['date_from'], '2023-01-01')
        self.assertEqual(response.context['rating'], '4')
