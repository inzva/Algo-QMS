from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from main.models import Problem, Submission


class ProblemList(ListView):
    model = Problem
    context_object_name = 'problems'
    template_name = 'problem.list.html'


class SubmissionForm(forms.Form):
    problem = forms.ModelChoiceField(Problem.objects.all())
    code = forms.CharField()


class ProblemDetail(LoginRequiredMixin, FormMixin, DetailView):
    model = Problem
    form_class = SubmissionForm
    context_object_name = 'problem'
    template_name = 'problem.detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProblemDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_absolute_url(self):
        return reverse('ProblemDetail', kwargs={'slug': self.pk})

    def get_object(self, queryset=None):
        problem_id = self.kwargs['pk']
        problem_detail = Problem.objects.get(id=problem_id)
        return problem_detail

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        problem = form.cleaned_data['problem']
        code = form.cleaned_data['code']

        submission = Submission.objects.create(user=self.request.user, problem=problem)

        from types import ModuleType
        compiled = compile(code, '', 'exec')
        module = ModuleType('dummymodule')
        exec(compiled, module.__dict__)

        for case in problem.testcase_set.all():
            module.__dict__['args'] = case.input
            output = eval('main(args)', module.__dict__)

            submission.submissiontestcaseresult_set.create(
                test_case=case,
                succeeded=(int(case.output) == output)
            )

        return super(ProblemDetail, self).form_valid(form)


class SubmissionList(LoginRequiredMixin, ListView):
    model = Submission
    context_object_name = 'submissions'
    template_name = 'submission.list.html'


class SubmissionDetail(LoginRequiredMixin, DetailView):
    model = Submission
    context_object_name = 'submission'
    template_name = 'submission.detail.html'
