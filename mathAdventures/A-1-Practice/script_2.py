def average(a,b):
    return (a + b) / 2

def mySum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum

print(mySum(100))

def mySum2(num):
    running_sum = 0
    for i in range(num + 1):
        running_sum += i**2 + 1
    return running_sum

print(mySum2(20))