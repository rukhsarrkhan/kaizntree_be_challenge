from rest_framework import serializers
from DashboardApp.models import Category, Tag, Item
from rest_framework.exceptions import ValidationError


class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except ValidationError as e:
            raise ValidationError("Invalid type, does not exist.") from e


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
    category = CustomPrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    tags = CustomPrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)

    class Meta:
        model=Item 
        fields=('id','sku','name','category','tags','stock_status','available_stock')
    
    def to_representation(self, instance):
        # Use the read-only serializers for reading
        representation = super(ItemSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        representation['tags'] = TagSerializer(instance.tags, many=True).data
        return representation

    def validate_category(self, value):
        # Custom validation logic for category
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError(f"Invalid category ID: {value.id}")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        category_data = validated_data.pop('category')
        item = Item.objects.create(**validated_data, category=category_data)
        item.tags.set(tags_data)  # Associate the tags using set()
        return item