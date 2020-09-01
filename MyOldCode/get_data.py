def get_data(filename):
    a = 0
    b = 0
    c = 0
    f = open(filename,'r')
    for line in f:
        a += 1
        wordList = line.split()
        for word in wordList:
            b += 1
        for character in line:
            c += 1
    return(a,b,c)

print(get_data('alice.txt'))
