n = int(input('Enter a positive integer n >= 3: '))
fiboOne = 1
fiboTwo = 1
for i in range(3,n + 1):
    fibo = fiboOne + fiboTwo
    fiboOne = fibo
    fiboTwo = fibo - fiboTwo
print(fibo)
