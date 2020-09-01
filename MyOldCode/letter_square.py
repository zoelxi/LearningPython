def letter_square(letter,size):
    assert size > 0, 'size: illegal argument'
    # assert letter.length == 1, 'letter: illegal argument'
    result = ''
    for i in range(size):
        for j in range(size):
            result = result + letter
        result = result + '\n'
    return result

print(letter_square('x', 5))
            
