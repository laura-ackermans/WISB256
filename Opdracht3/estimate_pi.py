import random
import math
import sys

def drop_needle(L): 
        x = random.random()
        a = random.vonmisesvariate(0,0)
        x2 = (x + L*math.cos(a))
        if x2 > 1 or x2 < 0: 
            return True
        else:
            return False

if len(sys.argv) != 4 and len(sys.argv) != 3:
    print("Use: estimate_pi.py N L")
elif float(sys.argv[2]) <= 0.0: 
    print("L should be lager than 0")
elif len(sys.argv) == 4:
    random.seed(int(sys.argv[3]))
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    hit = [False]*N
    i = 0
    while i < N: 
        hit[i] = drop_needle(L)
        i += 1
    numberofhits = hit.count(True)
    if L > 1: 
        pi = (2*L - 2*(math.sqrt(L*L-1) + math.asin(1/L)))/(numberofhits/N -1)
    else:
        pi = N*L*2/numberofhits
    print(str(numberofhits) +  " hits in " + str(N) + " tries")
    print("Pi = " + str(pi))
else:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    hit = [False]*N
    i = 0
    while i < N: 
        hit[i] = drop_needle(L)
        i += 1
    numberofhits = hit.count(True)
    if L > 1: 
        pi = (2*L - 2*(math.sqrt(L*L-1) + math.asin(1/L)))/(numberofhits/N -1)
    else:
        pi = N*L*2/numberofhits
    print(str(numberofhits) +  " hits in " + str(N) + " tries")
    print("Pi = " + str(pi))