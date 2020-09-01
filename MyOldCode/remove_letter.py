def remove_letter(string,letter):
    x=''
    for i in string:
        if i != letter:
            x += i
    return x


