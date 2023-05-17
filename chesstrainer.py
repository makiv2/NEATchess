import chess.engine
import neat
import numpy as np

from bitboard import board_to_3vector
from encoder import *
from fitness import *


def train_ai(genome1, genome2, config):
    # Create the neural networks
    print('Checkpoint 0.5')
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    board = chess.Board()

    vector = board_to_3vector(board)

    # add 5 helper nodes to the input layer, number of moves made, castle rights, el passant square, possbile legal moves, piece values, positional values, game phase, opponents last moves and legal moves.=
    print('Checkpoint 0.7')
    # Play the game
    while not board.is_game_over():

        # Determine whose turn it is
        if board.turn == chess.WHITE:
            output = net1.activate(vector)
            print('Checkpoint 1')
            moves = get_what_piece_to_move_priorities(output)
            print('Checkpoint 2')
            priorities = get_piece_to_move_priorities_to_indexes(moves)
            print('Checkpoint 3')
            pick_up_piece_at_index = evaluate_pick_up_square_probabilities(board, priorities, genome1)

            print("Move the piece at index: ", pick_up_piece_at_index)
            print('The piece to move is: ', board.piece_at(pick_up_piece_at_index))

            break



        else:
            output = net2.activate(vector)

        # Get the legal moves for the current player
        legal_moves = list(board.legal_moves)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

    # Return the winner
    # Update the fitness of the genomes


def get_move_type(data):
    # Calculate which move the AI wants to make
    pass


def evaluate_pick_up_square_probabilities(board, priorities, genome):
    for i in priorities:
        if board.piece_at(i) and board.piece_at(i).color == board.turn:
            return i
        else:
            genome.fitness -= 1