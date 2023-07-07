from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_contents/', views.get_contents, name='get_contents')
]
