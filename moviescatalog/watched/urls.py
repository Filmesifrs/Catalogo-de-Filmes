from django.urls import path
from .views import toggle_watched

urlpatterns = [
    path('toggle/', toggle_watched, name='toggle_watched'),
]