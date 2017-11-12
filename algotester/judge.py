import random
random.seed()


def judge(file_path, question):
    runTimeErrors = []
    timeLimitErrors = []
    correctAnswers = []
    wrongAnswers = []
    runningTimes = []
    numberOfTestCases = 10
    weights = 0
    for i in range(numberOfTestCases):
        weights.append(random.randint(0, 1000) / 1000)
    score = 0
    for i in range(numberOfTestCases):
        b = random.randint(0, 4)
        if(b == 0):
            runTimeErrors.append(0)
            timeLimitErrors.append(0)
            correctAnswers.append(1)
            wrongAnswers.append(0)
        elif(b == 1):
            runTimeErrors.append(0)
            timeLimitErrors.append(0)
            correctAnswers.append(0)
            wrongAnswers.append(1)
            score += weights[i]
        elif(b == 2):
            runTimeErrors.append(1)
            timeLimitErrors.append(0)
            correctAnswers.append(0)
            wrongAnswers.append(0)
        elif(b == 3):
            runTimeErrors.append(0)
            timeLimitErrors.append(1)
            correctAnswers.append(0)
            wrongAnswers.append(0)
            parameters = {"runTimeErrors": runTimeErrors,
                          "timeLimitErrors": timeLimitErrors, "correctAnswers": correctAnswers,
                          "wrongAnswers": wrongAnswers, "runningTimes": runningTimes, "score": score}
            return parameters
