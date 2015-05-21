def findRoot(f,a,b,epsilon): 
    m = (a+b)/2
    if f(a) == 0: 
        return a 
    elif f(b) == 0: 
        return b
    elif f(m) == 0: 
        return m
    elif f(a) > 0 and f(b) < 0 and abs(a - b) <= epsilon: 
        return m 
    elif f(a) < 0 and f(b) > 0 and abs(a - b) <= epsilon: 
        return m
    else:
        if f(a) > 0 and f(m) < 0: 
            return findRoot(f,a,m,epsilon)
        elif f(a) < 0 and f(m) > 0: 
            return findRoot(f,a,m,epsilon)
        elif f(m) < 0 and f(b) > 0: 
            return findRoot(f,m,b,epsilon)
        elif f(m) > 0 and f(b) < 0: 
            return findRoot(f,m,b,epsilon)
            
def findAllRoots(f,a,b,epsilon):
    roots = []
    n = int((b-a)/epsilon)
    for i in range(0,n): 
        if f(a+i*epsilon)*f(a+(i+1)*epsilon) <= 0:
            c = findRoot(f,a+i*epsilon,a+(i+1)*epsilon,epsilon)
            roots = roots + [c]
            i = i + 1
    return (list(set(roots)))