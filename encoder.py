from const import MOVEMAP
import numpy as np


def get_move_type_probability(output_tensor):
    means = []
    num_sets = len(output_tensor) // 64  # Calculate the number of sets of 72 elements

    for i in range(num_sets):
        start = i * 64  # Starting index of the set
        end = start + 64  # Ending index of the set
        subset = output_tensor[start:end]  # Extract the subset of 72 elements
        subset_mean = np.mean(subset)  # Calculate the mean of the subset
        means.append(subset_mean)  # Append the mean to the means array
    return means


def get_valid_moves(board, output_tensor):
    pass


def get_piece_to_move_priorities_to_indexes(move_priorities):
    indices_sorted = sorted(range(64), key=lambda i: move_priorities[i], reverse=True)[:64]
    return indices_sorted


def get_what_piece_to_move_priorities(output):
    arrays = [[] for _ in range(64)]
    means = []

    counter = 0
    for i in output:
        arrays[counter].append(i)
        counter += 1
        if counter == 64:
            counter = 0

    for array in arrays:
        mean = np.mean(array)
        means.append(mean)

    return means