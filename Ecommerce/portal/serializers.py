# serializers.py
from rest_framework import serializers
from .models import *

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['app_url', 'menu_name']

class MainMenuSerializer(serializers.ModelSerializer):
    ChildMenu = SubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = MainMenu
        fields = ['app_url', 'app_icon', 'menu_name', 'ChildMenu']
    


# class AdminLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserDetail
#         fields = '__all__'
