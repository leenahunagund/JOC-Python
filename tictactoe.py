import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s="X"
p2s="0"

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
            if(count==3):
                print(symbol,"Won")
                return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
            if(count==3):
                print(symbol,"Won")
                return True
    return False

def check_diagonals(symbol):
    if board[0][2]==board[1][1] or board[2][0]==board[1][1] or board[1][1]==symbol:
        print(symbol,"won")
        return True
    if board[0][0]==board[1][1] or board[2][2]==board[1][1] or board[1][1]==symbol:
        print(symbol,"won")
        return True
    return False
                      

def won(symbol):
    return check_rows(symbol) and check_cols(symbol) and check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    row=int(input("enter the row no.:1,2,3 : "))
    col=int(input("enter the column no.:1,2,3 : "))
    while(1):
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("wrong option enter again")
            break
    board[row-1][col-1]=symbol
    
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print("0 turn")
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print("draw")
play()