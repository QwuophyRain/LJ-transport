from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='update'),
    path('password_update/', views.user_password, name='password_update'),
    path('update_profile/', views.profileUpdate, name='update_profile'),
]