import chess
import numpy as np


def board_to_bitboard(board_state):
    bitboard = {}

    for piece_type in chess.PIECE_TYPES:
        for color in chess.COLORS:
            bitboard[piece_type, color] = board_state.pieces(piece_type, color)
    return bitboard


def bitboard_to_params(bitboard):
    params = []
    for piece_type in chess.PIECE_TYPES:
        for color in chess.COLORS:
            params.append(bitboard[piece_type, color])
    return params


def flatten_bitboards(bitboards):
    bitmaps = []
    for bitboard in bitboards:
        bitmaps.append(np.array(list(bitboards[bitboard]), dtype=np.uint8))
    bitvector = np.concatenate(bitmaps)
    return bitvector




