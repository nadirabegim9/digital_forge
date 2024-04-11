from django.urls import path
from .views import *

urlpatterns = [

    path('manager/', ManagerViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='manager_list'),
    path('manager/<int:pk>/', ManagerViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='manager_detail'),

    path('client/', ClientViewSets.as_view({'get': 'list'}),
         name='client_list'),
    path('client/<int:pk>/', ManagerViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='client_detail'),

    path('apartment/', ApartmentViewSets.as_view({'get': 'list'}),
         name='apartment_list'),
    path('apartment/<int:pk>/', ApartmentViewSets.as_view({'get': 'retrieve', 'put': 'update'}),
         name='apartment_detail'),

    path('review/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
]