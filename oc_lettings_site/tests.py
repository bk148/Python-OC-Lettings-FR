from django.test import TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def test_index(self):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_title(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Welcome to Holiday Homes")



