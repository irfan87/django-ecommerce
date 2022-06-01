from django.http import HttpRequest
from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from unittest import skip

from store.models import Category, Product
from store.views import all_products


@skip("run skip test")
class TestSkip(TestCase):
    def test_skip_test(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        Category.objects.create(name="test", slug="test")
        User.objects.create(username="admin")
        self.productData = Product.objects.create(
            category_id=1,
            title="test",
            created_by_id=1,
            slug="test",
            price="12.00",
            image="test",
        )

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.client.get(reverse("store:product_detail", args=["test"]))

        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """
        Test Category response status
        """
        response = self.client.get(reverse("store:category_list", args=["test"]))

        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/item/test")
        response = all_products(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
