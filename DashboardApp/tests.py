from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Category, Tag, Item
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemAPITests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(email='rukhsarkhan4198@gmail.com', password='loginpassword')
        # Create a category
        self.category = Category.objects.create(name='Electronics')
        # Create tags
        self.tag1 = Tag.objects.create(name='Portable')
        self.tag2 = Tag.objects.create(name='Battery Powered')
        # Create an item
        self.item = Item.objects.create(
            sku='123ABC', name='Portable Speaker', category=self.category, 
            stock_status=69, available_stock=10
        )
        self.item.tags.add(self.tag1, self.tag2)
        # Generate a token for the user
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_get_items(self):
        response = self.client.get(reverse('dashboardApi'), format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 1)   
    
    def test_get_item_by_id(self):
        response = self.client.get(reverse('dashboardApi-detail', kwargs={'id': self.item.id}), format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['name'], self.item.name)

    def test_create_item(self):
        data = {
        'sku': '456DEF', 
        'name': 'Smart Watch', 
        'category': self.category.id, 
        'tags': [self.tag1.id, self.tag2.id],
        'stock_status': 789.56, 
        'available_stock': 15
        }
        response = self.client.post(reverse('dashboardApi'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        created_item = Item.objects.latest('id')
        self.assertEqual(created_item.name, data['name'])
        self.assertEqual(created_item.stock_status, data['stock_status'])

    def test_update_item(self):
        data = {
            'sku': self.item.sku, 
            'name': 'Updated Portable Speaker', 
            'category': self.category.id, 
            'tags': [self.tag1.id, self.tag2.id],
            'stock_status': 0, 
            'available_stock': 0
        }
        response = self.client.put(reverse('dashboardApi-detail', kwargs={'id': self.item.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_item = Item.objects.get(id=self.item.id)
        self.assertEqual(updated_item.name, 'Updated Portable Speaker')

    def test_delete_item(self):
        response = self.client.delete(reverse('dashboardApi-detail', kwargs={'id': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0) 

class CategoryAPITests(APITestCase):

    def setUp(self):
        # Authentication setup
        self.user = User.objects.create_user(email='rukhsarkhan4198@gmail.com', password='loginpassword')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Create a category
        self.category = Category.objects.create(name='Electronics')

    def test_list_categories(self):
        response = self.client.get(reverse('categoryApi'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)  # Assuming this is the only category
    
    def test_get_category_by_id(self):
        response = self.client.get(reverse('categoryApi-detail', kwargs={'id': self.category.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], self.category.name)

    def test_create_category(self):
        data = {'name': 'Gadgets'}
        response = self.client.post(reverse('categoryApi'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Now there should be two categories

    def test_delete_category(self):
        response = self.client.delete(reverse('categoryApi-detail', kwargs={'id': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)  # Category should be deleted

class TagAPITests(APITestCase):

    def setUp(self):
        # Authentication setup
        self.user = User.objects.create_user(email='rukhsarkhan4198@gmail.com', password='loginpassword')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Create tags
        self.tag = Tag.objects.create(name='Portable')

    def test_list_tags(self):
        response = self.client.get(reverse('tagApi'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)  # Assuming this is the only tag

    def test_get_tag_by_id(self):
        response = self.client.get(reverse('tagApi-detail', kwargs={'id': self.tag.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], self.tag.name)

    def test_create_tag(self):
        data = {'name': 'Battery Powered'}
        response = self.client.post(reverse('tagApi'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 2)  # Now there should be two tags

    def test_delete_tag(self):
        response = self.client.delete(reverse('tagApi-detail', kwargs={'id': self.tag.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)  # Tag should be deleted

