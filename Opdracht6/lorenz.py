from scipy.integrate import odeint
import numpy
import math

class Lorenz: 
    
    def __init__(self,initial, sigma = 10, rho = 28, beta = 8/3):
        self.x = initial[0]
        self.y = initial[1]
        self.z = initial[2]
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.initial = initial
        
    def func(self, stap, t): 
        xt = stap[0]
        yt = stap[1]
        zt = stap[2]
        f0 = self.sigma*(yt - xt)
        f1 = xt*(self.rho - zt) - yt
        f2 = xt*yt - self.beta*zt
        return [f0, f1, f2]
 
    def solve(self, T,dt): 
        t = numpy.arange(0,T+dt,dt)
        solution = odeint(self.func, self.initial, t)
        return solution