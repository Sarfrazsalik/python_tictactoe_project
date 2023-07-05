board=["-","-","-",
       "-","-","-",
       "-","-","-"]
currentplayer="x"
winner=None
gamerunning=True

#Printing the game board

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printboard(board)


#Take player input

def playeerinput(board):
    inp=int(input("Enter a number in b/w 1 and 9: "))

    if inp >= 1 and inp <=9 and board[inp-1] == "-":
     board[inp-1]=currentplayer
    else:
       print("oops! its Already filled") 

#check for win or lose       
def check_horizontal(board):
   global winner    
   if board[0]==board[1]==board[2] and board[0]!="-":
    winner=board[0] 
    return True
   elif board[3]==board[4]==board[5] and board[3]!="-":
     winner=board[3]
     return True
   elif board[6]==board[7]==board[8] and board[6]!="-":
      winner=board[6]
      return True
   
def check_row(board):
   global winner
   if  board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0] 
        return True
      
   elif  board[1]==board[4]==board[7] and board[1]!="-":
         winner=board[1] 
         return True

   elif  board[2]==board[5]==board[8] and board[2]!="-":    
          winner=board[2] 
          return True  
def check_diagonal(board):
   global winner
   if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0] 
        return True
      
   elif board[2]==board[4]==board[6] and board[2]!="-":
         winner=board[2] 
         return True

def check_tie(board):
    if "-" not in board:
        printboard(board)
        print("its a Tie!")

#check win
def check_win():
#   global gamerunning
  if check_diagonal(board) or check_horizontal(board) or check_row(board):
      print(f"The Winner is {winner}") 
    #   gamerunning=False    

# Switch the player  

def switchplayer():
    global currentplayer
    if currentplayer == 'x':
       currentplayer = "o" 
    else:
        currentplayer = "x"  
        

while gamerunning:
   printboard(board)
   if winner != None:
        break
   playeerinput(board)
   check_win()
   check_tie(board)
   switchplayer()





               