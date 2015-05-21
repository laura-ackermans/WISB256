def findRoot(f,a,b,epsilon): 
    m = (a+b)/2
    if abs(a - b) <= epsilon: 
        return m
    elif f(a) == 0: 
        return a 
    elif f(b) == 0: 
        return b
    elif f(m) == 0: 
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