from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    path('create/<int:pk>', user_create_view, name='create_user'),
    path('sign-in', user_sign_in_view, name='login'),
    path('sign-out', logoutUser, name='logout'),

]
