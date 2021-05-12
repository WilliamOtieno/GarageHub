from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.

def mechanic(request):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Mechanic" == group_name:
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-id").filter(user = request.user)
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(appointment_with__icontains = q)
        else:
            appointment_list = appointment_list
            
        appointments = {
            "query": appointment_list,
            "user_name": user_name
        }
        return render(request, "mechanic.html", appointments)
    else:
        return redirect("http://localhost:8000/")


def mechanic_appointment_list(request):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Mechanic" == group_name:
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-id").filter(user = request.user)
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(date__icontains = q)
        else:
            appointment_list = appointment_list
            
        appointment_list = {
            "query": appointment_list,
            "user_name": user_name,
            "form": AppointmentForm(),
        }
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            saving = form.save(commit = False)
            saving.user = request.user
            saving.save()
            messages.success(request, 'Post Created Successfully.')
        return render(request, 'mechanic_create_appointment.html', appointments)
    else:
        return redirect('http://localhost:8000/')


def appointment_delete(request, id):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Mechanic" == group_name:
        single_appointment = Appointment.objects.get(id = id)
        single_appointment.delete()
        messages.success(request, 'Your profile was updated.')
        return redirect('http://localhost:8000/mechanic/create_appointment/')
    else:
        return redirect('http://localhost:8000/')

def mechanic_appointment_update(request, id):
    group_name = Group.objects.all().filter(user = request.user)
    group_name = str(group_name[0])
    if "Mechanic" == group_name:
        user_name = request.user.get_username()
        appointment_list = Appointment.objects.all().order_by("-id").filter(user = request.user)
        q = request.GET.get("q")
        if q:
            appointment_list = appointment_list.filter(date__icontains = q)
        else:
            appointment_list = appointment_list
        single_appointment = Appointment.objects.get(id = id)
        form = AppointmentForm(request.POST or None, instance = single_appointment)
        if form.is_valid():
            saving = form.save(commit = False)
            saving.user = request.user
            saving.save()
            messages.success(request, 'Post Created Successfully.')
            return redirect('http://localhost:8000/mechanic/create_appointment/')
        appointments = {
            "query": appointment_list,
            "user_name": user_name,
            "form": form
        }
        return render(request, 'mechanic_appointment_update.html', appointments)
    else:
        return redirect('http://localhost:8000/')