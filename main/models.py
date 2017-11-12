from django.conf import settings
from django.db import models

import os
from django.db.models.signals import post_save


class Problem(models.Model):
    question_name = models.TextField()
    statement = models.TextField()
    memory_limit = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.CharField(max_length=80)
    output = models.CharField(max_length=100)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.input


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubmissionTestCaseResult(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    succeeded = models.BooleanField()


def problem_saved(instance, *args, **kwargs):
    directory = "Problems" + os.sep
    if not os.path.exists(directory):
        os.makedirs(directory)
        os.chdir(directory)
    else:
        os.chdir(directory)
    os.makedirs(instance.question_name, exist_ok=True)
    os.chdir(".." + os.sep)


post_save.connect(problem_saved, sender=Problem)


class Question(models.Model):
    question_name = models.CharField(max_length=100)
    weights = models.CharField(max_length=300)
    max_score = models.IntegerField()


"""
class Team(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    question_scores = models.CharField(max_length=1000)
    ranking = models.IntegerField()
    # question_scores example  = "galaktik:15,pakif:25,wuba:0"

    def __str__(self):
        return self.username

    def getQuestionScore(self, qname):
        for questionName in self.question_scores.split(","):
            if(questionName.split(":")[0] == qname):
                return int(questionName.split(":")[1])

    def updateScore(self, newScore):
        self.score = newScore
        self.save()

    def updateQuestionScore(self, qname, newScore):
        temp1 = self.question_scores[:self.question_scores.find(qname)]
        preScore = getQuestionScore(qname)
        temp2 = self.question_scores[self.question_scores.find(
            qname) + 1 + len(qname) + len(str(preScore))]
        self.question_scores = temp1 + qname + ":" + str(newScore) + temp2
        self.save()
        if(newScore > preScore):
            updateScore(self.score + newScore - preScore)

"""
