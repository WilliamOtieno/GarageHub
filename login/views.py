from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.contrib.auth import logout


# Create your views here.

def group_check(request):
    group_name = Group.objects.all().filter(user = request.user) 
    group_name = str(group_name[0])

    if "Client" == group_name:
        return redirect("http://localhost:8000/client/")
    elif "Mechanic" == group_name:
        return redirect("http://localhost:8000/mechanic/")
        

def logout_view(request):
    logout(request)
    return redirect("http://localhost:8000/")
    

class register_mechanic(TemplateView):
    template_name = "register_mechanic.html"


class register_client(TemplateView):
    template_name = "register_client.html"