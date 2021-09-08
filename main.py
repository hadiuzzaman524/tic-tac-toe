import numpy as np
import random as rd

board=np.array([
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]
)
def setBoardX(x):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==x):
                board[i][j]='X'


def setBoardY(y):
    for i in range(3):
        for j in range(3):

            if(board[i][j]==y):
                board[i][j]='Y'


def drowBoard():
    print("")
    for i in range(3):

        for j in range(3):
            if(board[i][j]=="X"):

                print(f" \u001b[42;1m {board[i][j]} ", end="\u001b[0m")
            elif(board[i][j] == "Y"):
                print(f" \u001b[41;1m {board[i][j]} ", end="\u001b[0m")
            else:
                print(f" \u001b[45;1m {board[i][j]} ", end="\u001b[0m")
        print()
        print("")

#set and clear background color
print("")
print("\u001b[44;1m\u000c[Welcome to tic tac toe..!\u001b[0m")
drowBoard()
count=0
userinput=[]

while count<np.sqrt(9):
    count+=1
    x=input("\u001b[44;1m\u000c[Please choose your favorite number between(1-9):\u001b[0m ")
    while int(x) in userinput:
        x=input("\u001b[44;1m\u000c[Already used please choose another one:\u001b[0m ")
    userinput.append(int(x))
    setBoardX(x)


    y=rd.randint(1,9)
    while y in userinput:
        y=rd.randint(1,9)

    userinput.append(int(y))

    setBoardY(str(y))
    drowBoard()



name="X"
if((board[0][0]==name and board[0][1]==name and board[0][2]==name) or
    (board[1][0]==name and board[1][1]==name and board[1][2]==name) or
    (board[2][0]==name and board[2][1]==name and board[2][2]==name) or
    (board[0][0]==name and board[1][0]==name and board[2][0]==name) or
    (board[0][1]==name and board[1][1]==name and board[2][1]==name) or
    (board[0][2]==name and board[1][2]==name and board[2][2]==name) or
    (board[0][0]==name and board[1][1]==name and board[2][2]==name) or
    (board[2][0]==name and board[1][1]==name and board[0][2]==name) ):
    print("\u001b[44;1m\u000c[Congratulations! You win 😊 \u001b[0m")

else:

    print("\u001b[44;1m\u000c[You loose 😢 \u001b[0m")




