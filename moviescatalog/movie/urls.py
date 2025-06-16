import os
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),
]

urlpatterns += static('/movie_posters/', document_root=os.path.join(settings.BASE_DIR, 'movie_posters'))
