for n in range(100,1000):
    properDivs = []
    for i in range(1,n):
        if n % i == 0:
            properDivs.append(i)
    sumOfDivs = 0
    for div in properDivs:
        sumOfDivs += div
    if sumOfDivs == 2*n:
        print(n)


        
        
            
