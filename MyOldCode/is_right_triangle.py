def is_right_triangle(a,b,c):
    if c > b and c > a:
        return a*a + b*b == c*c
    elif b > c and b > a:
        return a*a + c*c == b*b
    elif a > c and a > b:
        return b*b + c*c == a*a

