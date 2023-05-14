import chess


def board_to_bitboard(board_state):
    bitboard = {}

    for piece_type in chess.PIECE_TYPES:
        for color in chess.COLORS:
            bitboard[piece_type, color] = board_state.pieces(piece_type, color)
    return bitboard
