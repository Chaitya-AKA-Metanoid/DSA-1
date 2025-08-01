#question1 leet code

def question_1(numbers):
    #expected output = [1, 3, 12, 0, 0]
    fast=0 
    slow = 0
    for fast in range(len(numbers)):
        if numbers[fast] ==0:
            numbers[slow], numbers[fast] = numbers[fast], numbers[slow]
            slow +=1
    
    return numbers

print(question_1([0, 1, 0, 3, 12]))

