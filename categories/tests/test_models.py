from django.test import TestCase
from .models import Category


class CategoryModelTestCase(TestCase):
  def setUp(self:
      self.category = Category.objects.create(naem='Teste Category')

  def test_category_creation(self):
    """
    Test if a category is created successfully
    """
    self.assertEqual(self.category.name, 'Test Category')

  def test_category_representation(self):
    """
    Teste the string representation of the category
    """
    self.assertEqual(str(self.category), 'Test Category')

  def test_category_ordering(self):
    """
    Test the ordering of categories
    """
    another_category = Category.objects.create(name='Another Category')
    self.assertLess(self.category.name, another_category.name)
