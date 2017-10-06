from django.contrib import admin

from main.models import Problem, TestCase, Submission, SubmissionTestCaseResult


class TestCaseInline(admin.TabularInline):
    model = TestCase


class ProblemAdmin(admin.ModelAdmin):
    inlines = (TestCaseInline,)


class SubmissionTestCaseResultInline(admin.TabularInline):
    model = SubmissionTestCaseResult


class SubmissionAdmin(admin.ModelAdmin):
    inlines = (SubmissionTestCaseResultInline,)


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Submission, SubmissionAdmin)
