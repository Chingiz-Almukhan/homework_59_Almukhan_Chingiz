from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tracker.forms import AddEditForm
from tracker.models import IssueTracker


# class AddView(TemplateView):
#     template_name = 'add_task.html'
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         form = AddEditForm()
#         context['form'] = form
#         return self.render_to_response(context)
#
#     def post(self, request, *args, **kwargs):
#         form = AddEditForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'add_task.html', context={'form': form})
#         task = form.save()
#         return redirect('main')

class AddView(CreateView):
    template_name = 'add_task.html'
    success_url = reverse_lazy('main')
    model = IssueTracker
    form_class = AddEditForm
