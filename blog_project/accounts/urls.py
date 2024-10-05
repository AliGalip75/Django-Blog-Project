from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', views.login_user, name='loginuser'),
    path('logout', views.logout_user, name='logoutuser'),
    path('register', views.register_user, name='registeruser'),
]