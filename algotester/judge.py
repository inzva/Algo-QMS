import random
random.seed()


def judge(file_path, question, numberOfTestCases, scores):
    runtime = []
    timelimit = []
    correct = []
    wrong = []
    score = 0
    for i in range(numberOfTestCases):
        b = random.randint(0, 4)
        if(b == 0):
            runtime.append(0)
            timelimit.append(0)
            correct.append(1)
            wrong.append(0)
        elif(b == 1):
            runtime.append(0)
            timelimit.append(0)
            correct.append(0)
            wrong.append(1)
            score += scores[i]
        elif(b == 2):
            runtime.append(1)
            timelimit.append(0)
            correct.append(0)
            wrong.append(0)
        elif(b == 3):
            runtime.append(0)
            timelimit.append(1)
            correct.append(0)
            wrong.append(0)
    return runTimeErrors, timeLimitErrors, correctAnswers, wrongAnswers, runningTimes, score
