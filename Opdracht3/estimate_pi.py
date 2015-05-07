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

if len(sys.argv) != 4:
    print("Use: estimate_pi.py N L S")
elif float(sys.argv[2]) > 1:
    print("AssertionError: L should be smaller than 1")
else:
    random.seed(int(sys.argv[3]))
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    hit = [False]*N
    i = 0
    while i < N: 
        hit[i] = drop_needle(L)
        i += 1
    numberofhits = hit.count(True)
    pi = N*L*2/numberofhits
    print(str(numberofhits) +  " hits in " + str(N) + " tries")
    print("Pi = " + str(pi))