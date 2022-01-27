from django.urls import path, include
from user.views import user_create_view, user_sign_in_view

urlpatterns = [
    path('create/<int:pk>', user_create_view),
    path('sign-in', user_sign_in_view),

]
