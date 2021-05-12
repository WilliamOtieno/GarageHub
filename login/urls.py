from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html'), name="home"),
    path('logout/', views.logout_view, name='logout'),
    path('group/', views.group_check, name='group'),
    path('register_mechanic/', views.register_mechanic, name='register_mechanic'),
    path('register_client/', views.register_client, name='register_client'),
]
