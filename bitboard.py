import chess


def create_bitboard_from_board(board):
    bitboard = [0] * 12
    print(bitboard)
    for square, piece in board.piece_map().items():
        piece_type = piece.piece_type
        color = piece.color
        index = 2 * color + piece_type - 1
        bitboard[index] |= chess.BB_SQUARES[square]
    return tuple(bitboard)
