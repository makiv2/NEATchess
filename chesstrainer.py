import chess.engine
import neat
from bitboard import board_to_bitboard, flatten_bitboards


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    board = chess.Board()

    bitboards = board_to_bitboard(board)
    bitvector = flatten_bitboards(bitboards)

    # add 5 helper nodes to the input layer, number of moves made, castle rights, el passant square, possbile legal moves, piece values, positional values, game phase, opponents last moves and legal moves.=

    # Play the game
    while not board.is_game_over():

        # Determine whose turn it is
        if board.turn == chess.WHITE:
            output = net1.activate(bitvector)
        else:
            output = net2.activate(bitvector)
        print(output)

        # Get the legal moves for the current player
        legal_moves = list(board.legal_moves)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

    # Return the winner
    # Update the fitness of the genomes
