from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tracker.forms import AddEditForm
from tracker.models import IssueTracker


class AddView(CreateView):
    template_name = 'add_task.html'
    success_url = reverse_lazy('main')
    model = IssueTracker
    form_class = AddEditForm
