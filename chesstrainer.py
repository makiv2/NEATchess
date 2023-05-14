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
            nn = net1
        else:
            nn = net2

        # Get the legal moves for the current player
        legal_moves = list(game.legal_moves)

        output = nn.activate(game)

        print(output)

        # If there are no legal moves, the game is over
        if len(legal_moves) == 0:
            break

        # Eval each legal move and choose the best one

        # Make the best move

    # Return the winner
    return genome1 if game.result() == '1-0' else genome2 if game.result() == '0-1' else None
    # Update the fitness of the genomes
