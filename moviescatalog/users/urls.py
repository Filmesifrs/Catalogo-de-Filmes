from django.urls import path
from .views import home, login_view, register_view, change_password

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('password-reset/', change_password, name='change_password'),
]
