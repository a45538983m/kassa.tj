from rest_framework import status
from rest_framework.test import APITestCase

from .models import Overhead, Product, Warehouse


class ProductApiTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(nameproduct='Хлеб', code=1)

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/api/v1/')

    def test_list_products(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['nameproduct'], 'Хлеб')

    def test_create_product(self):
        response = self.client.post(
            '/api/v1/products/', {'nameproduct': 'Молоко', 'code': 2}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_duplicate_code_rejected(self):
        response = self.client.post(
            '/api/v1/products/', {'nameproduct': 'Другое', 'code': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_warehouse_record(self):
        response = self.client.post(
            '/api/v1/warehouse/',
            {'namewar': self.product.id, 'price': '10.50', 'remainder': 5},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Warehouse.objects.count(), 1)

    def test_create_overhead(self):
        response = self.client.post(
            '/api/v1/overheads/',
            {'nameover': self.product.id, 'price': '9.99', 'quantity': 3},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Overhead.objects.count(), 1)

    def test_schema_generates(self):
        # Маршруты Swagger подключаются только при DEBUG=True,
        # поэтому проверяем генерацию схемы напрямую.
        from io import StringIO

        from django.core.management import call_command

        out = StringIO()
        call_command('spectacular', '--validate', stdout=out)
        self.assertIn('/api/v1/products/', out.getvalue())
