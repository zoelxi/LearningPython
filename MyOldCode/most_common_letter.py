def number_of_occurences(string,letter):
    x=''
    for i in string:
        if i == letter:
            x += i
    return len(x)

def most_common_letter(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    z = 0
    for letter in letters:
        x = number_of_occurences(string,letter)
        if x > z:
            z = x
            y = letter
    return y
                




        
            
            
