def gcd(a,b):
    if a >= b:
        if b == 0:
            return a
        else:
            return gcd(a-b,b)
    else:
        return gcd(b,a)
    

