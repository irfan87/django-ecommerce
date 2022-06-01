from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.catData = Category.objects.create(name="test", slug="test")

    def test_category_model_entry(self):
        # Test Category model data insertion / types / field attributes

        data = self.catData
        self.assertTrue(isinstance(data, Category))

        # Test Category model return name
        self.assertEqual(str(data), "test")


class TestProductsModel(TestCase):
    def setUp(self):
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

    def test_product_model_entry(self):
        # Test Product model data insertion / types / field attributes
        data = self.productData
        self.assertTrue(isinstance(data, Product))

        # Test Product model return name
        self.assertEqual(str(data), "test")
