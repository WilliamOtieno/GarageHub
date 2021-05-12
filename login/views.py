from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout

# Create your views here.
