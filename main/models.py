from django.conf import settings
from django.db import models


class Problem(models.Model):
    statement = models.TextField()
    memory_limit = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TestCase(models.Model):
    problem = models.ForeignKey(Problem)
    input = models.CharField(max_length=80)
    output = models.CharField(max_length=100)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.input


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    problem = models.ForeignKey(Problem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubmissionTestCaseResult(models.Model):
    submission = models.ForeignKey(Submission)
    test_case = models.ForeignKey(TestCase)
    succeeded = models.BooleanField()
