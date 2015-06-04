import math
primes = open('prime.dat', 'r')
string = primes.read()
lijst = [int(x) for x in string.split('\n')[0:-1]]
largest = lijst[-1]
numberofprimes = len(lijst)-1
nlogn = largest / math.log(largest)
ratio = numberofprimes / nlogn
print('Largest prime = ' + str(largest))
print('--------------------------------')
print('pi(N)         = ' + str(numberofprimes))
print('N/log(N)      = ' + str(nlogn))
print('ratio         = ' + str(ratio))
git 
twinprimes = []
for i in range(0,numberofprimes):
    if lijst[i] == lijst[i+1] - 2: 
        twinprimes = twinprimes + [lijst[i]]
    i = i + 1

C = 0.6601618
numberoftwins = len(twinprimes)
twinnlogn = 2 * C * largest / (math.log(largest)**2)
twinratio = numberoftwins / twinnlogn
print('--------------------------------')
print('pi_2(N)       = ' + str(numberoftwins))
print('2CN/log(N)^2  = ' + str(twinnlogn))
print('ratio         = ' + str(twinratio))