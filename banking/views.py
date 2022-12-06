from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Client, Account, Credit


class ClientListView(generic.ListView):
    model = Client
    template_name = 'xz.html'
    context_object_name = 'list_view'


class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = 'list'

