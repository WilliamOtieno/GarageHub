from django.urls import path
from . import views


urlpatterns = [
    path('', views.mechanic, name='mechanic_home'),
    path('my_appointment/', views.mechanic, name='mechanic_appointment'),
    path('create_appointment/', views.mechanic_appointment_list, name='mechanic_appointment_list'),
    path('create_appointment/delete/<int:id>/', views.appointment_delete, name='appointment_delete'),
    path('create_appointment/update/<int:id>/', views.mechanic_appointment_update, name='mechanic_appointment_update'),
]
