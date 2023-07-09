import solara
from .helpers import (
    get_board_values, 
    get_init_state, 
    check_winner,
    reset_game_state
)

####
# The solara state variables used to control the application
state = get_init_state()
turn = solara.reactive("X")
winner = solara.reactive("-")

def restart(): 
    reset_game_state(state)
    refresh()

def refresh(): 
    board = get_board_values(state)
    winner.set(check_winner(board))
    

@solara.component
def Cell(cell_value): 
    """Draw a cell of the Tic Tac Toe board with some value"""
    def set_cell_value(cell_value): 
        if cell_value.value == "-": 
            cell_value.set(turn.value)
            if turn.value=="X": 
                turn.set("O")
            else: 
                turn.set("X")
        refresh()
#        print(cell_value.value)
    solara.Button(cell_value.value, 
                  on_click =lambda:  set_cell_value(cell_value),
                  disabled=(winner.value!="-")
                  )
    
@solara.component    
def Grid(): 
    """Draw the tic tac toe grid"""
    with solara.Row(): 
        Cell(state[0][0])
        Cell(state[0][1])        
        Cell(state[0][2])                
    with solara.Row(): 
        Cell(state[1][0])
        Cell(state[1][1])        
        Cell(state[1][2])                
    with solara.Row(): 
        Cell(state[2][0])
        Cell(state[2][1])        
        Cell(state[2][2])                                
    solara.Info(f"Round to play : {turn.value}")    
    solara.Success(f"Winner : {winner.value}")    

@solara.component        
def Page(): 
    """Draw the app components"""
    solara.Title("Tic Tac Toe")
    with solara.Sidebar(): 
        #solara.Markdown("Tic Tac Toe")
        solara.Button("Restart", on_click=restart)
    with solara.Column():
        Grid()