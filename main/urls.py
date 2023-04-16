from django.urls import path, include
from .views import(
        index,
        login_view,
        logout_view,
        logout_after,
        registration_view,
        search_results,
        add_deal_adeguata,
        add_deal_anagrafica,
        registration_success,
        upload_files,
    )

urlpatterns = [
    path('index', index, name="index"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('logout_after', logout_after, name="logout-after"),
    path('register', registration_view, name="register"),
    path('search_results', search_results, name="search_results"),
    path('add_deal_adeguata', add_deal_adeguata, name="add_deal_adeguata"),
    path('add_deal_anagrafica', add_deal_anagrafica, name="add_deal_anagrafica"),
    path('registration_success', registration_success, name="registration_success"),
    path('upload_files', upload_files, name="upload_files"),
]
