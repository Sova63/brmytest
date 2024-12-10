from django.test import TestCase
from .models import SimpleModel


class SimpleModelTestCase(TestCase):
	def test_create_simple_model(self):
		# Создаем объект модели
		obj = SimpleModel.objects.create(name="Test Name")

		# Проверяем, что объект создан корректно
		self.assertEqual(obj.name, "Test Name")
		self.assertEqual(SimpleModel.objects.count(), 1)
