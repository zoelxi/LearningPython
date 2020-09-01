def print_board(tttList):
    '''print_board(tttList) -> None
    prints a tic-tac-toe board corresponding to tttList'''
    print(tttList[0]+'|'+tttList[1]+'|'+tttList[2])  
    print('-+-+-')                                   
    print(tttList[3]+'|'+tttList[4]+'|'+tttList[5])  
    print('-+-+-')                                  
    print(tttList[6]+'|'+tttList[7]+'|'+tttList[8]) 

print_board([' ', 'O', 'X', ' ', 'X', 'X', ' ', 'O', 'O'])
