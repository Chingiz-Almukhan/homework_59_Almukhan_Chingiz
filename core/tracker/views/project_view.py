from django.views.generic import DetailView

from tracker.models import Project
from tracker.models.issue_tracker import IssueTracker


class ProjectDetailView(DetailView):
    template_name = 'project_view.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['tasks'] = IssueTracker.objects.filter(project=self.kwargs['pk'])
        print(context['tasks'])
        return context
