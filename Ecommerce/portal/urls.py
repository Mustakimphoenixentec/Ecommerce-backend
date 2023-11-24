# urls.py
from django.urls import path
# from .views import *
from . import views
# from .views import *

urlpatterns = [
    path('get_email/', views.get_email, name='get_user'),
    path('get_menu/', views.menu_data, name='get_menu'),
    # path('user-details/<int:pk>/', UserDetailRetrieveUpdateDestroyView.as_view(), name='user-detail-retrieve-update-destroy'),
]
