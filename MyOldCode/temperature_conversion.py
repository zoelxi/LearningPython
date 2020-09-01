def fahrenheit_to_celsius(f):
    c = (5/9)*(f-32)
    return c

def celsius_to_fahrenheit(c):
    f = 32 + (9/5)*c
    return f

print(fahrenheit_to_celsius(32))

print(celsius_to_fahrenheit(0))
