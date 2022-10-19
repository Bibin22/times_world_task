from django.urls import path
from .views import *
urlpatterns = [
    path('',user_login, name='user_login'),
    path('user_creation',user_creation, name='user_creation')
]