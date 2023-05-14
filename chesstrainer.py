import chess.engine
import neat
from bitboard import board_to_bitboard


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    board = chess.Board()
    bitboard = board_to_bitboard(board)

    wp = int(bitboard[1, True])
    bp = int(bitboard[1, False])
    wn = int(bitboard[2, True])
    bn = int(bitboard[2, False])
    wb = int(bitboard[3, True])
    bb = int(bitboard[3, False])

    # Play the game
    while not board.is_game_over():

        # Determine whose turn it is
        if board.turn == chess.WHITE:
            output = net1.activate((wp, wn, wb))
        else:
            output = net2.activate((bp, bn, bb))
        print(output)

        # Get the legal moves for the current player
        legal_moves = list(board.legal_moves)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

    # Return the winner
    # Update the fitness of the genomes
