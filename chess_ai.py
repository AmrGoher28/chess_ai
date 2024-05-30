import chess
import random


   
piece_values = {
    'P': 1,   # Pawn
    'N': 3,   # Knight
    'B': 3,   # Bishop
    'R': 5,   # Rook
    'Q': 9,   # Queen
    'K': 100,  # King 
    '.': 0,  # Empty square
    'p': -1,  # Pawn (white)
    'n': -3,  # Knight (white)
    'b': -3,  # Bishop (white)
    'r': -5,  # Rook (white)
    'q': -9,  # Queen (white)
    'k': -100  # King (white)
}

  
def evaluation_function(board):
    evaluationWhite = 0
    evaluationBlack = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.color == chess.WHITE:
                evaluationWhite += piece_values[piece.symbol()]
            else:
                evaluationBlack += piece_values[piece.symbol()]

    return evaluationWhite + evaluationBlack



# implementinf min max algorithm 
def minimax(board, depth, maximizingPlayer):
    if depth == 0 or board.is_game_over():
        return None, evaluation_function(board)

    best_move = None

    if maximizingPlayer:
        value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            _, new_value = minimax(board, depth - 1, False)
            board.pop()
            if new_value > value:
                value = new_value
                best_move = move
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            _, new_value = minimax(board, depth - 1, True)
            board.pop()
            if new_value < value:
                value = new_value
                best_move = move

    return best_move, value

    
def main():
    board = chess.Board()

    print("Welcome to Chess against Random AI!")
    print(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            user_move = input("Enter your move : ")
            try:
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    board.push(move)
                    print(board)
                else:
                    print("Invalid move Please try again.")
            except ValueError:
                print("Invalid input Please enter a valid move.")
        else:
            ai_move, _ = minimax(board, 3, False)
            if ai_move is not None:
                board.push(ai_move)
                print("AI's move:", ai_move)
                print(board)

    print("Game over.")
    print("Result: " + board.result())



if __name__ == "__main__":
    main()
