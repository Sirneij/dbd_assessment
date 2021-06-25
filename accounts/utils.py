from django.contrib.auth import authenticate
from rest_framework import serializers


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user

def create_user_account(email, password, first_name="",
                        last_name="", phone="", avatar="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, phone=phone, avatar=avatar, **extra_fields)
    return user