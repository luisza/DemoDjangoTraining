from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse


class viewsTest(TestCase):

    def test_index_only_by_post(self):
        response = self.client.get(reverse("var1mipk", kwargs={'var1': 1, 'mipk': 'a0b1ff' }))
        self.assertEqual(response.status_code, 405)

    def test_index_without_params(self):
        response = self.client.get(reverse("index" ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "UPS FALTAN COSAS")

    def test_index_without_params(self):
        response = self.client.get(reverse("index" )+"?var1=12&mipk=a0b1ff")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Es válido")