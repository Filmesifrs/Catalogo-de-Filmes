from django.urls import path
from .views import home, login_view, register_view, logout_view, change_password, perfil, minhas_avaliacoes

app_name = "users"

urlpatterns = [
  path('', home, name='home'),
  path("perfil/", perfil, name="perfil"),
  path("avaliacoes/", minhas_avaliacoes, name="minhas_avaliacoes"),
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register'),
  path('password-reset/', change_password, name='change_password'),
  path('logout/', logout_view, name='logout'),
]
