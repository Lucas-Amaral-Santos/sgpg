"""sgpg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from registrar.views import logar, logout_view
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aluno/',include('aluno.urls', namespace='aluno')),
    path('professor/',include('professor.urls', namespace='professor')),
    path('matricula/',include('matricula.urls', namespace='matricula')),
    path('disciplina/',include('disciplina.urls', namespace='disciplina')),
    path('evento/',include('evento.urls', namespace='evento')),
    path('relatorios/',include('relatorios.urls', namespace='relatorios')),
    path('config/',include('config.urls', namespace='config')),
    path('logar/', logar, name='logar'),
    path('sair', logout_view, name='logout_view')
    ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
