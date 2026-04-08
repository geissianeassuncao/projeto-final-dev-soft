"""
URL configuration for elderlink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from appelderlink.views import home
from appelderlink.views import login_view, home, paciente_home, medico_home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/' , include('appelderlink.urls')),

    path("login/", login_view, name="login"),

    path("paciente/home/", paciente_home, name="paciente_home"),
    path("medico/home/", medico_home, name="medico_home"),

    path('reset/', auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset_form.html'
), name='password_reset'),

path('reset_enviado/', auth_views.PasswordResetDoneView.as_view(
    template_name='registration/password_reset_done.html'
), name='password_reset_done'),

path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='registration/password_reset_confirm.html'
), name='password_reset_confirm'),

path('reset_concluido/', auth_views.PasswordResetCompleteView.as_view(
    template_name='registration/password_reset_complete.html'
), name='password_reset_complete'),
]
