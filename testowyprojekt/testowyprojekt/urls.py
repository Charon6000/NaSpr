"""
URL configuration for testowyprojekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from testowaapka.views import Uczniowie, Klasy, FormularzDodawaniaUcznia, FormularzEdytowaniaUcznia, UczniowieDetale, UczniowieList, FormularzDodawaniaKlas, UsuwanieKlas
from django.contrib.auth import views

urlpatterns = [
    # path('login/', views.LoginView.as_view(template_name='testowaapka/login.html'), name="login"),
    path('admin/', admin.site.urls),
    path('', Uczniowie, name="uczniowie"),
    path('klasy/', Klasy, name="klasy"),
    path('uczniowie/', Uczniowie, name="uczniowie"),
    path('dodajucznia/', FormularzDodawaniaUcznia, name="FormularzDodawaniaUcznia"),
    path('edytujucznia/<int:id>', FormularzEdytowaniaUcznia, name="FormularzEdytowaniaUcznia"),
    path('dodajklase/', FormularzDodawaniaKlas, name="FormularzDodawaniaKlas"),
    path('Detale/<int:pk>', UczniowieDetale.as_view(), name="Uczen CB"),
    path('ListaUczniow', UczniowieList.as_view(), name="Uczen CB"),
    path('usuwanieklas', UsuwanieKlas, name="usuwanieklas"),
    # path('accounts/', include('django.contrib.auth.urls')),
]
