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


def board_to_3vector(board):
    bitboards = board_to_bitboard(board)
    vector = []

    for bitboard in bitboards.values():
        bitstream = bin(int(bitboard))
        binary_str = bitstream[2:]
        padded_str = "{:0>64}".format(binary_str)
        for x in padded_str:
            vector.append(int(x))

    halfmove = bin(board.halfmove_clock)
    binary_halfmove = halfmove[2:]
    padded_halfmove = "{:0>64}".format(binary_halfmove)
    for x in padded_halfmove:
        vector.append(int(x))

    fullmove = bin(board.fullmove_number)
    binary_fullmove = fullmove[2:]
    padded_fullmove = "{:0>64}".format(binary_fullmove)
    for x in padded_fullmove:
        vector.append(int(x))
    return vector
