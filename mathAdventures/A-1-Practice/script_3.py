# Conditionals
y = 7
if y > 5:
    print('yes!')

age = 50
if age < 10:
    print('What school do you go to?')
elif 11 < age < 20:
    print("You're cool!")
elif 20 <= age < 30:
    print("What job do you have?")
elif 30 <= age < 40:
    print('Are you married?')
else:
    print("Wow, you're old!")

# Factors.py function
def factors(num):
    '''returns a list of the factors of num'''
    factorList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList

print(factors(120))

# Greatest common factor (GCF)
def gcf(num1, num2):
    list1 = factors(num1)
    list2 = factors(num2)
    gcfList = []
    for i in list1:
        if i in list2:
            gcfList.append(i)
    return max(gcfList) 

print(gcf(150,138))

# wander.py
from turtle import *
from random import randint

speed(0)

def wander():
    while True:
        forward(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            left(randint(90, 180))

wander()