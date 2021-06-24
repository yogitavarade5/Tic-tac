# Tic tac,toe Game
a =[[1,2,3],[4,5,6],[7,8,9]]
player=1
symbol='X'
tr=0
fw=False
while True:
    i=0
    while i<=2:
        j=0
        while j<=2:
            print(a[i][j],end=" ")
            j=j+1
        print()
        i=i+1


    print("play your turn player",player)
    print("your symbol=",symbol)
    print("Enter box number")
    box=int(input())
    if box==1:
         a[0] [0] = symbol
    elif box==2:
         a[0] [1] =symbol
    elif box==3:
         a[0] [2] =symbol
    elif box==4:
         a[1] [0] =symbol
    elif box==5:
         a[1] [1]=symbol
    elif box==6:
         a[1] [2]=symbol
    elif box==7:
         a[2] [0]=symbol
    elif box==8:
         a[2] [1]=symbol
    elif box==9:
         a[2] [2]=symbol
    if   a[0] [0]==a[0] [1] and a [0][1]==a[0][2]:
         print("player",player,"Wins...!")
         fw=True
         break
    elif  a[1][0]==a[1][1] and a[1][1]== a[1][2]:
        print("player",player,"wins!..")
        fw=True
        break
    elif  a[2][0]==a[2][1] and a[2][1]==a[2][2]:
        print("player",player,"Wins..!")
        fw=True
        break
    elif a[0][0]==a[1][0] and a[1][0]==a[2][0]:
         print("player",player,"Wins!")
         fw=True
         break
    elif  a[0][1]==a[1][1] and a[1][1]==a[2][1]:
        print("player",player,"Wins!")
        fw=True
        break
    elif a[0][2]==a[1][2] and a[1][2]==[2][2]:
        print("player",player,"Wins!")
        fw=True
        break
    elif a[0][0]==a[1][1] and a[1][1]==a[1][2]:
        print("player",player,"Wins!")
        fw=True
        break
    elif a[0][2]==a[1][1] and a [1][1]==a[2][0]:
        print("player,",player,"Wins!")
        fw=True
        break
    if  player==1:
        player=2
        symbol="O"
    elif player==2:
        player=1
        symbol="X"




















