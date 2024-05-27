import chess


board=chess.Board()
print(board)


# listing all the legal moves in a given state
legal_moves = list(board.legal_moves)
for move in legal_moves:
    print(move)


# pick the best move from the list of legal moves
    
piece_values = {
    'p': -1,  # Pawn
    'n': -3,  # Knight
    'b': -3,  # Bishop
    'r': -5,  # Rook
    'q': -9,  # Queen
    'k': -100,  # King (considerably large negative value to prioritize king's safety)
    'P': 1,   # Pawn
    'N': 3,   # Knight
    'B': 3,   # Bishop
    'R': 5,   # Rook
    'Q': 9,   # Queen
    'K': 100,  # King (considerably large positive value to prioritize opponent's king's safety)
    '.': 0    # Empty square
}

evaluation = sum(piece_values.get(piece, 0) for row in board for piece in row)
print("Evaluation:", evaluation)
