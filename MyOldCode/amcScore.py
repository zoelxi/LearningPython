numAnswered = int(input("Enter the number of questions answered: "))
numCorrect = int(input("Enter the number of questions correct: "))
score = numCorrect*6 + (25-numAnswered)*1.5
print("The student's score is: " + str(score))
