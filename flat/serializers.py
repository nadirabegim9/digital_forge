from rest_framework import serializers
from .models import Manager, Apartment, Review, Client


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'full_name', 'phone', 'email', 'temporary_password')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'manager', 'apartment', 'review_text', 'date')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field="full_name", queryset=Client.objects.all())

    class Meta:
        model = Apartment
        fields = '__all__'


# class ReviewSerializer(serializers.ModelSerializer):
#     parent = serializers.PrimaryKeyRelatedField(queryset=Reviews.objects.all(), required=False, allow_null=True)
#     product = serializers.SlugRelatedField(slug_field="name", queryset=Product.objects.all())
#     user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
#
#     class Meta:
#         model = Reviews
#         fields = ('id', 'user', 'text', 'stars', 'data', 'parent', 'product')
#
