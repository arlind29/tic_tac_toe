import solara

def reset_game_state(state): 
    """Reset game state"""
    for row in state: 
        for cell in row: 
            cell.set("-")
    
def get_init_state(): 
    """Get initial game state"""
    init_matrix = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

    state = []
    for init_row in init_matrix: 
        row = []
        for value in init_row: 
            row.append(solara.reactive(value))
        state.append(row)
    return state

def check_winner(board):
    """Check for winner of the game

    Args:
        board (list): board representation of the game
    Returns:
        str: the winner, "-" means no winner, otherwise "X" or "O" 
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "-":
            return row[0]
    
    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != "-" for row in range(len(board))):
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    
    # No winner
    return "-"

def get_board_values(state): 
    """Get board values as a list of list of string values"""
    board = []
    for init_row in state: 
        row = []
        for cell in init_row: 
            row.append(cell.value)
        board.append(row)
    return board 