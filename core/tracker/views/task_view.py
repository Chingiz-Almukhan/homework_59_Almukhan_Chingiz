from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from tracker.models.issue_tracker import IssueTracker


# class TaskView(TemplateView):
#     template_name = 'task_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = get_object_or_404(IssueTracker, pk=kwargs['pk'])
#         return context

class TaskView(DetailView):
    template_name = 'task_view.html'
    model = IssueTracker
    context_object_name = 'task'
