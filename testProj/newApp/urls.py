from . import views
from django.urls import path 

urlpatterns = [
   path('Home/', views.Home, name = 'Home')
]
