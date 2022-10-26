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

print(equation(2,5,0,13))
print(equation(12,18,-34,67))

x = equation(12,18,-34,67)

print(12*x+18)
print(-34*x + 67)