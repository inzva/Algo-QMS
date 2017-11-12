import subprocess
import sys
import os
import time
from abc import ABC
from .models import Question
python3Ext = "py"
python2Ext = "py2"
cExt = "c"
cppExt = "cpp"
bashExt = "sh"
cSharpExt = "cs"


class JudgeMech:
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore):
        self.inpath = inpath
        self.outpath = outpath
        self.sesoutpath = sesoutpath
        self.question = question
        self.weights = weights
        self.runTimeErrors = []
        self.timeLimitErrors = []
        self.correctAnswers = []
        self.wrongAnswers = []
        self.runningTimes = []
        self.maxscore = maxscore

    @abstractmethod
    def specialPart():
        return None

    def checkanswers():
        total = 0.0
        for i in range(1, len(os.listdir(inpath)) + 1):
            if(self.runTimeErrors[i - 1] == 0):
                if(self.timeLimitErrors[i - 1] == 0):
                    file1 = open(outpath + "output" +
                                 str(i) + ".txt").readlines()
                    file2 = open(sesoutpath + "output" +
                                 str(i) + ".txt").readlines()
                    flag = 1
                    for j in range(len(file1)):
                        if(file1[j] != file2[j]):
                            flag = 0
                    if(flag == 1):
                        self.correctAnswers.append(1)
                        self.wrongAnswers.append(0)
                        total += self.weights[i]
                    else:
                        self.wrongAnswers.append(1)
                        self.correctAnswers.append(0)
        self.score = (total / sum(weights)) * self.maxscore

    def judge():
        specialPart()
        subprocess.call(["mkdir " + self.sesoutpath], shell=True)
        for i in range(1, len(os.listdir(self.inpath)) + 1):
            timeb = time.time()
            try:
                subprocess.run([self.shellscript], shell=True,
                               timeout=self.timelimit, check=True)
                self.timeLimitErrors.append(0)
                self.runTimeErrors.append(0)
            except subprocess.TimeoutExpired:
                self.timeLimitErrors.append(1)
                self.runTimeErrors.append(0)
            except subprocess.CalledProcessError:
                self.runTimeErrors.append(1)
            self.runningTimes.append(time.time() - timeb)
        self.checkanswers()
        if(self.execf != None):
            subprocess.call(["rm -rf " + execf], shell=True)
        subprocess.call(["rm -rf " + sesoutpath], shell=True)
        parameters = {"runTimeErrors": self.runTimeErrors,
                      "timeLimitErrors": self.timeLimitErrors, "correctAnswers": self.correctAnswers,
                      "wrongAnswers": self.wrongAnswers, "runningTimes": self.runningTimes, "score": self.score}
        return parameters


class Python3(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=10):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | python3 " + os.getcwd() + os.sep +
            filename + ">" + sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit

    def specialPart():
        return None


class Python2(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=10):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | python " + os.getcwd() + os.sep +
            filename + ">" + sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit

    def specialPart():
        return None


class C(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=2, execf="a.out"):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | ./a.out >" +
            sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit
        self.execf = execf
        self.subscript = "gcc " + os.getcwd() + os.sep +
            filename + "-o" + self.execf

    def specialPart():
        subprocess.run([self.subscript], shell=True,
                       timeout=30, check=True)


class CPP(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=2, execf="a.out"):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | ./a.out >" +
            sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit
        self.execf = execf
        self.subscript = "g++ " + os.getcwd() + os.sep +
            filename + "-o" + self.execf

    def specialPart():
        subprocess.run([self.subscript], shell=True,
                       timeout=30, check=True)


class Bash(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=2, execf="a.out"):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | bash " + os.getcwd() + os.sep +
            filename + ">" + sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit

    def specialPart():
        return None


class CS(JudgeMech):
    def __init__(inpath, outpath, sesoutpath, question, weights, maxscore, timelimit=2, execf="hello.exe"):
        super.__init__(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
        self.shellscript = "cat " + inpath + "input" + str(i) + ".txt | mono " + self.execf + " >" +
            sesoutpath + "output" + str(i) + ".txt"
        self.timelimit = timelimit
        self.execf = execf
        self.subscript = "mcs -out:" + self.execf +" + os.getcwd() +
            os.sep + filename

    def specialPart():
        subprocess.run([self.subscript], shell=True,
                       timeout=30, check=True)


def creator(extension, inpath, outpath, sesoutpath, question, weights):
    if(extension == python3Ext):
        judgeIns = Python3(inpath, outpath, sesoutpath,
                           question, weights, maxscore)
    elif(extension == python2Ext):
        judgeIns = Python2(inpath, outpath, sesoutpath,
                           question, weights, maxscore)
    elif(extension == cExt):
        judgeIns = C(inpath, outpath, sesoutpath,
                     question, weights, maxscore)
    elif(extension == cppExt):
        judgeIns = CPP(inpath, outpath, sesoutpath,
                       question, weights, maxscore)
    elif(extension == bashExt):
        judgeIns = Bash(inpath, outpath, sesoutpath,
                        question, weights, maxscore)
    return JudgeIns


def parser(username, filename, qname):

    extension = filename.split(".")[1]
    inpath = os.getcwd() + os.sep + qname + os.sep + "inputs" + os.sep
    outpath = os.getcwd() + os.sep + qname + os.sep + "outputs" + os.sep
    sesoutpath = os.getcwd() + os.sep + qname + os.sep + username + os.sep
    question = Question.objects.get(question_name=qname)
    weights = map(int, question.weights.split(","))
    maxscore = question.maxscore
    judgeIns = creator(extension, inpath, outpath,
                       sesoutpath, question, weights, maxscore)
    return judgeIns


def qualify(username, filename, qname):
    judgeIns = parser(username, filename, qname)
    return judgeIns.judge()
