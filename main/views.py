from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView

from main.models import Problem, Submission


class ProblemList(ListView):
    model = Problem
    context_object_name = 'problems'
    template_name = 'problem.list.html'


class ProblemDetail(DetailView):
    model = Problem
    context_object_name = 'problem'
    template_name = 'problem.detail.html'

    def get_absolute_url(self):
        return reverse('ProblemDetail', kwargs={'slug': self.pk})


class SubmissionList(LoginRequiredMixin, ListView):
    model = Submission
    context_object_name = 'submissions'
    template_name = 'submission.list.html'


class SubmissionDetail(LoginRequiredMixin, DetailView):
    model = Submission
    context_object_name = 'submission'
    template_name = 'submission.detail.html'
