print("Welcome to Connect 4")

def check_winner(board, player):
    for row in range(6):
        for col in range(6):
            
            # Horizontal check
            if col <= 2:
                if all(board[row][col + i] == player for i in range(4)):
                    return True
                
            # Vertical check
            if row <= 2:
                if all(board[row + i][col] == player for i in range(4)):
                    return True
                
            # Diagonal check to the bottom right
            if row <= 2 and col <= 2:
                if all(board[row + i][col + i] == player for i in  range(4)):
                    return True
                
            #Diagonal check to the bottom left
            if row <= 2 and col >= 3:
                if all(board[row + i][col - i] == player for i in range(4)):
                    return True
                
    return False

def make_board(board):
    print(" 1  2  3  4  5  6")
    print("------------------")
    
    for row in board:
        print(" " + " ".join(row))
    print("------------------")
    
def connect_4():
    ready = input("Are you ready(yes / no)? ")
    if ready.lower() != "yes":
        print("Ops!, See you later.")
        return
    
    board = [['o ' for n in range(6)] for n in range(6)]
    
    #Number of moves to detect a draw
    move = 0
    max_move = 36
    
    make_board(board)
    
    while True: 
        #Yellow player turn
        print("Yellow Piece")
        col_input = input("Column Selection: ")
        
        if not col_input.isdigit() or not (1 <= int(col_input) <= 6):
            print("Invalid input. Please enter a number 1 to 6.")
            continue
        
        # 0 index
        col = int(col_input) - 1
        
        #check from bottom to top to see if the cell is empty
        place = False
        for row in range(5, -1, -1):
            if board[row][col] == 'o ':
                board[row][col] = 'Y '
                place = True
                break
            
        if not place:
            print("This column is full. Please choose another column.")
            continue
        
        #incrementing the moves counter
        move += 1
        make_board(board)
        
        if check_winner(board, 'Y '):
            print("Yellow has won.")
            break
        
        #Checking for a draw condition
        if move == max_move:
            print("The game ended in a draw.")
            break
        
        #Red player turn
        #the following codes are similar to the yellow piece
        print("Red Piece")
        col_input = input("Column Selection: ")
        
        if not col_input.isdigit() or not (1 <= int(col_input) <= 6):
            print("Invalid input. Please enter a number 1 to 6.")
            continue
        
        col = int(col_input) - 1
        
        place = False
        for row in range(5, -1, -1):
            if board[row][col] == 'o ':
                board[row][col] = 'R '
                place = True
                break
            
        if not place:
            print("This column is full. Please choose another column.")
            continue
        
        move += 1
        make_board(board)
        
        if check_winner(board, 'R '):
            print("Red has won.")
            break
        
        if move == max_move:
            print("The game ended in a draw.")
            break
        
        
connect_4()


