import time
T1 = time.perf_counter()

import sys

primefile = open(sys.argv[2], 'w')

N = int(sys.argv[1])

isPrime = [False, False] + [True]*(N-1)
    
# zoek eerst instantie van True, 
# zet indices deelbaar door eerste op False, 
# loop voor zoekbegin groter dan eerste instantie.

for i in range(2,N+1): 
    if isPrime[i] != False:
        for j in range(2*i,N+1,i):
            isPrime[j]=False
            
# maak lijst met priemgetallen
primes = []

for i in range(2, N+1):
    if isPrime[i] == True: 
        primes.append(i)

# schrijf priemgetallen naar file

for i in range(0, len(primes)): 
   primefile.write(str(primes[i]) + '\n')

T2 = time.perf_counter()
print('Found ' + str(len(primes)) + ' Prime numbers smaller than ' + str(N) + ' in ' + str(T2 - T1) + ' sec.')