def print_welcome():
    """Print the welcome message."""
    print("Welcome to Minichess - A small-scale chess game!")
    print("Rules are based on the Los Alamos chess variant.\n")

def get_game_mode():
    """Prompt the user to select the game mode."""
    while True:
        mode = input("Choose Game Mode: 1 for 2-Player, 2 for 1-Player vs CPU: ").strip()
        if mode == '1':
            return "2P"
        elif mode == '2':
            return "CPU"
        else:
            print("Invalid input. Please enter 1 or 2.")

def check_for_checkmate(board, color):
    """Check if the given color has been checkmated (placeholder)."""
    # TODO: Add checkmate logic
    return False

def check_for_stalemate(board):
    """Check if the game has ended in a stalemate (placeholder)."""
    # TODO: Add stalemate logic
    return False

def print_game_over(winner):
    """Print a game over message."""
    print(f"Game Over! {winner} wins the game!")

def algebraic_to_index(pos):
    """
    Converts algebraic notation like 'a2' to board indices (row, col).
    E.g., 'a2' -> (6, 0)
    """
    files = 'abcdefgh'
    if len(pos) != 2 or pos[0] not in files or not pos[1].isdigit():
        raise ValueError("Invalid position format.")
    
    col = files.index(pos[0])
    row = 8 - int(pos[1])
    return row, col

def index_to_algebraic(index):
    """
    Converts board indices (row, col) to algebraic notation.
    E.g., (6, 0) -> 'a2'
    """
    files = 'abcdefgh'
    row, col = index
    return f"{files[col]}{8 - row}"
