from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'text', 'product', 'user']


    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('rating must be between 1 and 5')
        return value



class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='review_set', many=True, read_only=True)
    review_count = serializers.SerializerMethodField()

    category_data = CategorySerializer(source='category', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    owner_data = UserSerializer(source='owner', read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='owner',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category_data', 'category_id', 'owner_data', 'owner_id', 'review_count', 'reviews',
        ]

    def get_review_count(self, obj):
        return obj.review_set.count()
    



    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('price must be greater than 0')
        return value


    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('title cant be empty')
        return value
