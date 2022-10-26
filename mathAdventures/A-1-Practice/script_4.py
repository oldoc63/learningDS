#plug() function
def plug():
    x = -100 #start at -100
    while x < 100: #go up to 100
        if 2*x+5 == 13: #if it makes the equation true
            print("x =", x) #print it out
        x += 1 #make x go up by one to test the next number

plug()
