from django.shortcuts import render, redirect
from mechanic.models import Appointment
from mechanic.forms import AppointmentForm
from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.

def quick_appointment(request):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Client" == group_name:
        user_name =  request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-user")
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(user__first_name__icontains = q)
        else:
            appointment_list = appointment_list
        appointments = {
            "query": appointment_list,
            "user_name": user_name
        }
        return render(request, 'client_quick_appointment.html', appointments)
    else:
        return redirect('http://localhost:8000/')


def client(request):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Client" == group_name:
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with = user_name)
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(user__first_name__icontains = q)
        else:
            appointment_list = appointment_list
        appointments = {
            "query": appointment_list,
            "username": user_name
        }
        return render(request, 'client.html', appointments)
    else:
        return redirect('http://localhost:8000/')
    
def appointment_book(request, id):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Client" == group_name:
        user_name = request.user.get_username()
        single_appointment = Appointment.objects.get(id = id)
        form = single_appointment
        form.appointment_with = user_name
        form.save()
        messages.success(request, "Appointment Booked Successfully.")
        return redirect('http://localhost:8000/client/')
    else:
        return redirect('http://localhost:8000/') 
