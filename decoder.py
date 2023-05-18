import numpy as np
from const import MOVEMAP

def index_output(output):
    return sorted(range(output), key=lambda i: output[i], reverse=True)


def decode_move_from_index(index_array):
    moves = {}
    index_array = [5, 64, 126, 77, 4, 5, 6, 7]
    movemap = {v: k for k, v in MOVEMAP.items()}

    for i in index_array:
        move_group = i // 64
        square_index = i % 64
        moves[square_index] = movemap[move_group]

    return moves
