import chess.engine
import neat
import numpy as np

from bitboard import board_to_3vector
from encoder import *
from const import MOVEMAP
from decoder import *
from helpers import *


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    board = chess.Board()

    # Encode the board to a input vector
    board_vector = board_to_3vector(board)

    # Play the game
    while not board.is_game_over():

        if board.turn == chess.WHITE:

            # Get output for the white pieces
            output = net1.activate(board_vector)

            # Get moves
            moves = get_moves(output)

            # Find a valid move
            move = find_valid_move(board, moves)

            make_move(board, move)

            print('Made first move')
            print(board)

            break



        else:
            output = net2.activate(board_vector)

        # Get the legal moves for the current player
        legal_moves = list(board.legal_moves)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

    # Return the winner
    # Update the fitness of the genomes


def evaluate_pick_up_square_probabilities(board, priorities, genome):
    for i in priorities:
        if board.piece_at(i) and board.piece_at(i).color == board.turn:
            return i
        else:
            genome.fitness -= 1


# def get_move_type(data):
#     moves_to_make = []
#     move_type_probabilities = get_move_type_probability(data)
#     indexes_to_which_move_in_move_map = sorted(range(len(move_type_probabilities)),
#                                                key=lambda i: move_type_probabilities[i], reverse=True)
#
#     print(MOVEMAP)  # map index to movemap
#
#     return indexes_to_which_move_in_move_map


def simple_fitness_eval(board, genome1, genome2):
    if board.is_checkmate:
        if board.turn == chess.BLACK:
            genome1.fitness *= 1.5
            genome2.fitness *= 0.8
        else:
            genome1.fitness *= 1.5
            genome2.fitness *= 0.8


def is_move_legal(board, move):
    if move in board.legal_moves:
        return True
    else:
        return False


def find_valid_move(board, moves):
    print(moves)
    for move in moves:

        temp = create_move(move, moves[move])
        if is_move_legal(board, temp):
            return temp


def make_move(board, move):
    pass
