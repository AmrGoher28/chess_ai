import chess


# custom_starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPQPPPP/RNBQKBNR b KQkq - 0 1"

custom_starting_position = "rnbqkbnr/ppp1pppp/8/8/8/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1"


# Create a board object and set it to the custom starting position
board = chess.Board()
board.set_fen(custom_starting_position)

print(board)





# pick the best move from the list of legal moves
   
piece_values = {
    'P': 1,   # Pawn
    'N': 3,   # Knight
    'B': 3,   # Bishop
    'R': 5,   # Rook
    'Q': 9,   # Queen
    'K': 100,  # King (considerably large positive value to prioritize opponent's king's safety)
    '.': 0    # Empty square
}



# this will evaluate 
def evaluation_function(board):
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.color == chess.WHITE:
            evaluation = evaluation + piece_values[piece.symbol()]

    return evaluation


def best_move(board):
    best_eval = 140
    best_move = None

    # listing all the legal moves in a given state
    # legal_moves = list(board.legal_moves)
    for move in board.legal_moves:
        board.push(move)
        current_eval = evaluation_function(board)
        board = chess.Board()
        board.set_fen(custom_starting_position)
        if current_eval <= best_eval:
            best_eval = current_eval
            best_move = move

    return best_move

print(best_move(board))

    
    
