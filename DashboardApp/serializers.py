from rest_framework import serializers
from DashboardApp.models import Category, Tag, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category 
        fields=('id','name')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag 
        fields=('id','name')

class ItemSerializer(serializers.ModelSerializer):
    # Add nested serializers
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model=Item 
        fields=('id','sku','name','category','tags','stock_status','available_stock')