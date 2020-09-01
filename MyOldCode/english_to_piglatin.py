def english_to_piglatin(word):
    '''english_to_piglatin(word) -> string
    Translates word into Pig Latin.'''
    if word[0] in 'aeiouAEIOU':  # check if the first letter is a vowel
        return word + 'way'
    # word begins with a consonant
    consonants = ''  # keep track of consonants at start of word
    while len(word) > 0 and word[0] not in 'aeiouAEIOU':
        if word[0].isupper:
            consonants += word[0].lower() # add the consonant
            word = word[1:]        # remove the first letter from word
        else:
            consonants += word[0]
            word = word[1:]
    word = word[0].upper() + word[1:]
    return word + consonants + 'ay'

    






