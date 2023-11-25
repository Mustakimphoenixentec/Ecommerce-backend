# urls.py
from django.urls import path
# from .views import *
from . import views
# from .views import *

urlpatterns = [
    path('LoginAuth', views.get_email, name='email_login_api'),
    path('UserLogin', views.UserLoginAPIView, name='login_auth'),
    path('getMenuMappings', views.menu_data, name='get_menu'),
    # path('user-details/<int:pk>/', UserDetailRetrieveUpdateDestroyView.as_view(), name='user-detail-retrieve-update-destroy'),
]
