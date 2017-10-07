from django.views.generic import DetailView, ListView

from main.models import Problem


class ProblemList(ListView):
    model = Problem
    context_object_name = 'problems'
    template_name = 'problem.list.html'


class ProblemDetail(DetailView):
    model = Problem
    context_object_name = 'problem'
    template_name = 'problem.detail.html'

    def get_absolute_url(self):
        return reverse('ProblemDetail', kwargs={ 'slug' : self.pk })
