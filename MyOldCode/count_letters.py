def count_letters(text,letter):
    text=list(text)
    textLength=len(text)
    x=0
    count=0
    while x<textLength:
        if text[x]==letter:
            count+=1
        x+=1
    return count

print(count_letters("It's passed on. This parrot is no more. It has ceased to be. It's expired and gone to meet its maker. This is a late parrot. It's a stiff. Bereft of life, it rests in peace. If you hadn't nailed it to the perch, it would be pushing up the daisies. It's rung down the curtain and joined the choir invisible. This is an ex-parrot!","e"))



    
