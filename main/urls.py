from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('search_results', views.search_results, name="search_results"),
]
