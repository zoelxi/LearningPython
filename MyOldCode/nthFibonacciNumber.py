N = 16          

fib = []        
fib.append(0)   
fib.append(1)
x = 0
for i in range(N-2):
    fib.append(fib[x] + fib[x+1])
    x += 1

print(fib)  
