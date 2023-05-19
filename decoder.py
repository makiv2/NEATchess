import numpy as np
from const import MOVEMAP


def index_output(output):
    return sorted(range(len(output)), key=lambda i: output[i], reverse=True)


def decode_move_from_index(index_array):
    moves = []
    movemap = {v: k for k, v in MOVEMAP.items()}

    for i in index_array:

        move_group = i // 64
        square_index = i % 64
        moves.append((square_index, movemap[move_group]))
    return moves


def get_moves(output):
    indexes = index_output(output)
    return decode_move_from_index(indexes)
