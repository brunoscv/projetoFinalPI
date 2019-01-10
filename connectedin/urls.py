"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, \
    PasswordResetDoneView

from django.urls import path, include
from perfis import views
from usuarios.views import*

from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar', views.recusar, name='recusar'),
    path('convite/<int:perfil_id>/desfazer', views.desfazer_amizade, name='desfazer'),
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('mudar-senha/', views.mudar_senha, name="mudar_senha"),
    path('timeline/', include('timeline.urls'), name="timeline"),
    path('perfil/<int:perfil_id>/super', views.definirSuperUser, name='super'),
    path('perfil/post_new', views.post_new, name='post_new'),
    path('perfil/pesquisar', views.PesquisarPerfilView.as_view(), name='pesquisar'),
    path('password_reset/$', PasswordResetView.as_view(template_name='reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='reset_email.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/$', PasswordResetCompleteView.as_view(template_name='reset_password.html'),
         name='password_reset_complete'),
]


