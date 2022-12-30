import random



def main():
    board = []

    play_game = True

    init_board(board)

    for i in range(2):
        add_random_number(board)
    

    while (play_game):
        print_board(board)

        user_input = input("Use W, A, S, D to move (up, left, down, right): \n")
        while not (user_input.lower() == "w" or 
                   user_input.lower() == "a" or 
                   user_input.lower() == "s" or 
                   user_input.lower() == "d" or
                   user_input.lower() == "q"):
            print_board(board)
            user_input = input("Invalid response.\nUse W, A, S, D to move (up, left, down, right): \n")
        
        if user_input.lower() == 'q': 
            play_game = False
        else:
            det_shift_direction_do(board, user_input)
            add_random_number(board)



def det_shift_direction_do(board, user_input_direction):
    is_up =    user_input_direction.lower() == "w"
    is_down =  user_input_direction.lower() == "s"
    is_left =  user_input_direction.lower() == "a"
    is_right = user_input_direction.lower() == "d"
    board_hash = []
    init_board(board_hash)
    for i in range(0,3):
        if is_up:    shift_up(board,board_hash)
        if is_down:  shift_down(board,board_hash)
        if is_left:  shift_left(board,board_hash)
        if is_right: shift_right(board,board_hash)



def shift_right(board,board_hash):
    for y in range(0,4):
        for x in range(2,-1,-1):
            if (board[y][x + 1] == board[y][x] and board[y][x] > 0 and board_hash[y][x] == 0): 
                board[y][x + 1] = board[y][x + 1] + board[y][x]
                board[y][x] = 0
                board_hash[y][x + 1] = 1
                board_hash[y][x] = 0
            elif (board[y][x + 1 ] == 0 ):
                board[y][x + 1 ] = board[y][x] 
                board[y][x] = 0
                board_hash[y][x + 1] = board_hash[y][x] 
                board_hash[y][x] = 0



def shift_left(board,board_hash):
    for x in range(1,4):
        for y in range(0,4):
            if (board[y][x - 1] == board[y][x] and board[y][x] > 0 and board_hash[y][x] == 0): 
                board[y][x - 1] = board[y][x - 1] + board[y][x]
                board[y][x] = 0
                board_hash[y][x - 1] = 1
                board_hash[y][x] = 0
            elif (board[y][x - 1 ] == 0 ):
                board[y][x - 1 ] = board[y][x] 
                board[y][x] = 0
                board_hash[y][x - 1] = board_hash[y][x] 
                board_hash[y][x] = 0


def shift_down(board,board_hash):
    for y in range(2,-1,-1):
        for x in range(0,4):
            if (board[y + 1][x] == board[y][x] and board[y][x] > 0 and board_hash[y][x] == 0): 
                board[y + 1][x] = board[y + 1][x] + board[y][x]
                board[y][x] = 0
                board_hash[y + 1][x] = 1
                board_hash[y][x] = 0
            elif (board[y + 1][x] == 0 ):
                board[y +1 ][x] = board[y][x] 
                board[y][x] = 0
                board_hash[y +1 ][x] = board_hash[y][x] 
                board_hash[y][x] = 0

def shift_up(board,board_hash):
    for y in range(1,4):
        for x in range(0,4):
            if (board[y - 1][x] == board[y][x] and board[y][x] > 0 and board_hash[y][x] == 0): 
                board[y - 1][x] = board[y - 1][x] + board[y][x]
                board[y][x] = 0
                board_hash[y - 1][x] = 1
                board_hash[y][x] = 0
            elif (board[y - 1][x] == 0 ):
                board[y - 1][x] = board[y][x] 
                board[y][x] = 0
                board_hash[y - 1][x] = board_hash[y][x] 
                board_hash[y][x] = 0


    

def add_random_number(board):
    new_numbers = [2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2]
    next_number =new_numbers[random.randint(0,12)] 
    random_x_coor = random.randint(0,3)
    random_y_coor = random.randint(0,3)
    while (board[random_x_coor][random_y_coor] > 0):
        random_x_coor = random.randint(0,3)
        random_y_coor = random.randint(0,3)

    board[random_x_coor][random_y_coor] = next_number



def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print(f"[{' ': ^4}]", end = "")
            else:
                print(f"[{cell: ^4}]", end = "")
        print()



def init_board(board_gen):
    for i in range(4):
        row = [] 
        for j in range(4):
            row.append(0)
        board_gen.append(row)




if __name__ == '__main__':
    main()