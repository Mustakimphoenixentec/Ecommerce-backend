from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@csrf_exempt
def get_email(request):
    if request.method == 'GET':
        email = request.GET.get('Email')  # Use this if you're sending the email in the request body
        try:
            user_exists = User.objects.filter(email=email).exists()
            if user_exists:
                response_data = {'ErrorCode': '5', 'Result': 'archKey'}
                return JsonResponse(response_data)
            else:
                return JsonResponse({'ErrorCode': '0', 'Result': 'Invalid Email'})

        except Exception as e:
            return JsonResponse({'ErrorCode': '500', 'Result': 'Internal Server Error'})




def menu_data(request):
    if request.method == 'GET':
        role_id = request.GET.get('role_id')

        # Query main menu and related submenus using Django models
        main_menus = MainMenu.objects.filter(role_id=role_id)
        menu_data = {}

        for main_menu in main_menus:
            main_menu_key = f"{main_menu.id}_{main_menu.app_url}_{main_menu.app_icon}_{main_menu.menu_name}"
            sub_menus = SubMenu.objects.filter(main_menu_ref_id=main_menu)
            
            sub_menu_list = [{"AppUrl": sub_menu.app_url, "MenuName": sub_menu.menu_name} for sub_menu in sub_menus]
            
            menu_data[main_menu_key] = {
                "AppUrl": main_menu.app_url,
                "AppIcon": main_menu.app_icon,
                "MenuName": main_menu.menu_name,
                "RoleID": main_menu.role_id.id,
                "ChildMenu": sub_menu_list
            }

        # Extract the values from the dictionary
        result_values = list(menu_data.values())

        return JsonResponse({"MenuItems": result_values})
