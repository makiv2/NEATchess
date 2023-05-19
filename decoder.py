import numpy as np
from const import MOVEMAP


def index_output(output):
    return sorted(range(len(output)), key=lambda i: output[i], reverse=True)


def decode_move_from_index(index_array):
    moves = {}
    movemap = {v: k for k, v in MOVEMAP.items()}

    print(index_array)
    print(movemap)
    for i in index_array:

        move_group = i // 64
        square_index = i % 64
        moves[square_index] = movemap[move_group]
        #print('The index element: ', i, 'is in the move group: ', move_group, 'and the square index is: ', square_index)
    print(moves)

    return moves


def get_moves(output):
    indexes = index_output(output)
    return decode_move_from_index(indexes)
