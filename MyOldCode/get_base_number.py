def get_base_number(num,base):
    if len(num) == 0:
        return 0
    else:
        return int(num[0])*(base**(len(num)-1)) + get_base_number(num[1:],base)

print(get_base_number('10011',2))  # should be 19
print(get_base_number('3202',5))   # should be 427
print(get_base_number('611023',7))
