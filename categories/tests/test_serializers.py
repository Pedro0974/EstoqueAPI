from django.test import TestCase
from .models import Category
from .serializers import CategorySerializer


class CatregorySerializerTestCase(TestCase):
  def setUp(self):
    self.category_data = {'name': 'Test Category'}
    self.category = Category.objects.create(name='Test Category')
    self.serializer = CategorySerializer(instance=self.category)

  def test_serializer_contains_expexted_fields(self):
    """
    Test if the serializer contains the expected fields
    """
    data = self.serializer.data
    self.assertEqual(set(data.keys()), {'id', 'name', 'created_in', 'modified_in', 'ativo'}

  def test_serializer_create_valid(self):
    """
    Test if the serializer creates a valid category instance.
    """
    serializer = CategorySerializer(data=self.category_data)
    self.assertTrue(serializer.is_valid())
    category_instance = serializer.save()
    self.assertIsInstance(category_instance, Category)

  def test_serializer_update_valid(self):
      """
      Test if the serializer updates a valid category instance.
      """
      serializer = CategorySerializer(instance=self.category, data={'name': 'Updated Category'})
      self.assertTrue(serializer.is_valid())
      category_instance = serializer.save()
      self.assertEqual(category_instance.name, 'Updated Category')
