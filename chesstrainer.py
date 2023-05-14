import chess.engine
import neat


def train_ai(genome1, genome2, config):
    # Create the neural networks
    net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    # Create the chess board
    game = chess.Board()

    # Play the game
    while not game.is_game_over():

        # Determine whose turn it is
        if game.turn == chess.WHITE:

            output = net1.activate(game)
        else:

            output = net2.activate(game)

        # Get the legal moves for the current player
        legal_moves = list(game.legal_moves)

        print(output)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

    # Return the winner
    return genome1 if game.result() == '1-0' else genome2 if game.result() == '0-1' else None
    # Update the fitness of the genomes


def board_to_bitboard(board_state):
    bitboard = 0
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            bitboard += piece.piece_type * 2 ** i
    return bitboard