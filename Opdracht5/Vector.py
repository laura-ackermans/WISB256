import math

class Vector: 
    
    def __init__(self,n,values): 
        if type(values) != list: 
            self.vector = [values]*n
        else: 
            self.vector = values
    
    def __str__(self):
        self.string = ''
        for i in range(0,len(self.vector)):
            self.string = self.string + str(self.vector[i]) + '\n'
        return self.string
    
    def lincomb(self,other,alpha,beta): 
        scaledsum = [0]*len(self.vector)
        for i in range(0,len(self.vector)): 
            scaledsum[i] = alpha * self.vector[i] + beta * other.vector[i]
        return Vector(len(self.vector),scaledsum)
    
    def scalar(self,alpha): 
        scaled = [0]*len(self.vector)
        for i in range(0,len(self.vector)):
            scaled[i] = alpha * self.vector[i]
        return Vector(len(self.vector),scaled)
        
    def inner(self,other): 
        inproduct = 0
        for i in range(0,len(self.vector)): 
            inproduct = inproduct + self.vector[i]*other.vector[i]
        return inproduct
        
    def norm(self): 
        lengte2 = 0
        for i in range(0,len(self.vector)): 
            lengte2 = lengte2 + self.vector[i]**2
        lengte = math.sqrt(lengte2)
        return lengte