for xyz in range(100,1000):
    z = xyz % 10
    y = (xyz // 10) % 10
    x = (xyz // 100)
    
    if xyz % 11 == 0 and xyz/11 == z*z + y*y + x*x:
        print(xyz)


