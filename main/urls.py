from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.registration_view, name="register"),
    path('search_results', views.search_results, name="search_results"),
    path('add_deal', views.add_deal, name="add_deal"),
    path('registration_success', views.registration_success, name="registration_success"),
]
