#plug() function
def plug():
    x = -100 #start at -100
    while x < 100: #go up to 100
        if 2*x+5 == 13: #if it makes the equation true
            print("x =", x) #print it out
        x += 1 #make x go up by one to test the next number

#plug()

#algebra.py
def equation(a,b,c,d):
    '''solves equations of the form ax + b = cx + d'''
    return (d-b)/(a-c)

# print(equation(2,5,0,13))
# print(equation(12,18,-34,67))

# x = equation(12,18,-34,67)

# print(12*x+18)
# print(-34*x + 67)
# print((1/2),(2/3),(1/5),(7/8))
# print(equation(.5, .66667, 0.2, 0.875))

#quad.py
from math import sqrt

def quad(a,b,c):
    '''Returns the solutions of an equation of the form a*x**2 +b*x + c = 0'''
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2
