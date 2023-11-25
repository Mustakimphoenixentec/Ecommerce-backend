from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import jwt


@csrf_exempt
def get_email(request):
    if request.method == 'GET':
        email = request.GET.get('Email')    
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

        result_values = list(menu_data.values())

        return JsonResponse({"MenuItems": result_values})

def generate_jwt_token(data, secret_key):
    try:
        token = jwt.encode(data, secret_key, algorithm='HS256')
        return token
    except Exception as e:
        print(f"Error generating JWT token: {str(e)}")
        return None

# views.py
@csrf_exempt
def UserLoginAPIView(request):
    if request.method == 'GET':
        user_email = request.GET.get('Email')
        user_password = request.GET.get('password')   
        try:
                user = User.objects.get(email=user_email, password=user_password)
                userdetaildata = UserDetail.objects.get(user_ref_id = user.id)
                token = TokenMaster.objects.get(user_ref_id = user.id)
                main_menus = MainMenu.objects.filter(role_id=userdetaildata.role_ref_id.id)
                menu_data = {}

                user_data_dict = {
                "email": user.email,
                "password": user.password
                }
                
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

                result_values = list(menu_data.values())
                        # Update LoginToken if needed
                
                secret_key1 = "django-insecure-c*pwled-#2hs!vfhg=s(odv-w2y-22kgx)_laf_xy70!49rx1r"
                token.user_access_token = generate_jwt_token(user_data_dict, secret_key1)  # Implement your token generation logic here
                token.save()

                response_data = {
                'ErrorCode': '1',
                'FName': user.first_name,
                'LName': user.last_name,
                'LoginToken': token.user_access_token,
                'UserId': user.id,
                'RoleCode': userdetaildata.role_ref_id.id,
                'MenuItems': [result_values]
                }
                return JsonResponse(response_data)

        except User.DoesNotExist:
                return JsonResponse({'message': 'User not found or authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)

    return JsonResponse({'message': 'This not not correct method'}, status=status.HTTP_400_BAD_REQUEST)
