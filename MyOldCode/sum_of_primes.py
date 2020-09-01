def is_multiple(x,y):
    return (x % y == 0)

def is_prime(n):
    isPrime = True  
    for div in range(2, int(n**0.5) + 1):
        if is_multiple(n, div):
            isPrime = False
    return isPrime

def sum_of_primes(x):
    z=0
    sumOfPrimes=0
    n=2
    while z<x:
        if is_prime(n) == True:
            sumOfPrimes+=n
            z+=1
        n+=1
    return sumOfPrimes

print(sum_of_primes(100))
        
