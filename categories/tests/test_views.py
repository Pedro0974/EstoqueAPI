from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateAPIViewTestCase(APITestCase):
  def setUp(self):
    self.category_data = {'name': 'TestCategory'}
    self.category = Category.objects.create(name='Test Categpry')

  def test_create_category(self):
    """
    Test if a new category can be created via API
    """
    url = reverse('categories')
    response = self.client.post(url, self.category_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Category.objects.count(), 2)

  def test_list_categories(self):
    """
    Test if categories can be listed via API
    """
    url = reverse('categories')
    response = self.client.get(url)
    self.assertEqual(response.staatus_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_filter_categories(self):
      """
      Test if categories can be filtered via API.
      """
      url = reverse('category-list')
      response = self.client.get(url, {'name': 'Test'})
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 1)

class CategoryRetrieveUpdateAPIViewTestCase(APITestCase):
    def setUp(self):
      self.category = Category.objects.create(name='Test Category')

    def test_retrieve_category(self):
      """
      Test if a category can be retrieved via API.
      """
      url = reverse('category-detail', kwargs={'pk': self.category.pk})
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data['name'], 'Test Category')

    def test_update_category(self):
      """
      Test if a category can be updated via API.
      """
      url = reverse('category-detail', kwargs={'pk': self.category.pk})
      updated_data = {'name': 'Updated Category'}
      response = self.client.put(url, updated_data, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(Category.objects.get(pk=self.category.pk).name, 'Updated Category')

    def test_delete_category(self):
      """
      Test if a category can be deleted via API.
      """
      url = reverse('category-detail', kwargs={'pk': self.category.pk})
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertEqual(Category.objects.count(), 0)
