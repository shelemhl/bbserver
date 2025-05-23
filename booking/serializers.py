# bookingbite/booking/serializers.py


# Importing serializers from the common app
from common.serializers import DateSerializer, DishSerializer, DateHasDishSerializer



# from rest_framework import serializers
# from chef_management.models import DateSaved, DateHasDish, Dish


# class DateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DateSaved
#         fields = ['date_saved']

# class DishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dish
#         fields = ['dish_id', 'dish_name', 'dish_description', 'dish_type', 'dish_calories', 'light_healthy', 'sugar_free']

# class DateHasDishSerializer(serializers.ModelSerializer):
#     date_has_dish_id = serializers.IntegerField(source='pk')  # Add date_has_dish_id field
#     date_saved = DateSerializer()  # Using nested serializer for DishDate
#     dish = DishSerializer(source='dish_id')  # Using nested serializer for Dish

#     class Meta:
#         model = DateHasDish
#         fields = ['date_has_dish_id', 'date_saved', 'dish', 'quantity']
#         extra_kwargs = {
#             'quantity': {'required': False}  # Make quantity optional
#         }

