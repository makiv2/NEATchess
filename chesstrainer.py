import chess.engine
import neat
import numpy as np

from bitboard import board_to_3vector
from encoder import *


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    board = chess.Board()

    vector = board_to_3vector(board)

    # add 5 helper nodes to the input layer, number of moves made, castle rights, el passant square, possbile legal moves, piece values, positional values, game phase, opponents last moves and legal moves.=

    # Play the game
    while not board.is_game_over():

        # Determine whose turn it is
        if board.turn == chess.WHITE:
            output = net1.activate(vector)



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

