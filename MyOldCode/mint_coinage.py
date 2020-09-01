def mint_coinage(d1,d2,d3):
    if d1 > d2:
        (d1,d2) = (d2,d1)
    if d2 > d3:
        (d2,d3) = (d3,d2)
    numCoins = []
    for change in range(100):
        count = 0
        while change > 0:
            if change >= d3:
                change -= d3
            elif change >= d2:
                change -= d2
            elif change >= d1:
                change -= d1
            count += 1
        numCoins.append(count)
    print(numCoins)
    total = 0
    for num in numCoins:
        total += num
    averageNum = total/100
    return averageNum


print(mint_coinage(1,10,25))
                
            
        
