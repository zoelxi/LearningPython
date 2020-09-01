def find_winner(tttList):
    string = 'X'
    if string == tttList[0] == tttList[1] == tttList[2] or string == tttList[3] == tttList[4] == tttList[5] or string == tttList[6] == tttList[7] == tttList[8] or string == tttList[0] == tttList[3] == tttList[6] or string == tttList[1] == tttList[4] == tttList[7] or string == tttList[2] == tttList[5] == tttList[8] or string == tttList[0] == tttList[4] == tttList[8] or string == tttList[2] == tttList[4] == tttList[6]:
        return string
    string = 'O'
    if string == tttList[0] == tttList[1] == tttList[2] or string == tttList[3] == tttList[4] == tttList[5] or string == tttList[6] == tttList[7] == tttList[8] or string == tttList[0] == tttList[3] == tttList[6] or string == tttList[1] == tttList[4] == tttList[7] or string == tttList[2] == tttList[5] == tttList[8] or string == tttList[0] == tttList[4] == tttList[8] or string == tttList[2] == tttList[4] == tttList[6]:
        return string

print(find_winner(['O', ' ', ' ', ' ', 'O', 'X', ' ', 'O', 'O']))
