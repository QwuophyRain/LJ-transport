from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('addtobuscart/<int:id>', views.addtobuscart, name='addtobuscart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderbus/', views.orderbus, name='orderbus'),

]