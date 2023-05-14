import neat
import chess


def evaluate_population(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i + 1]:
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            # Initialize game

            # New function
            game = chess.Board()
            net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
            net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
            while not game.is_game_over():
                if game.turn:
                    move = net1.activate(game)
                else:
                    move = net2.activate(game)
                game.push(chess.Move.from_uci(str(move)))
            if game.is_checkmate():
                if game.turn:
                    genome1.fitness += 1
                else:
                    genome2.fitness += 1
            elif game.is_stalemate():
                genome1.fitness += 0.5
                genome2.fitness += 0.5
            else:
                genome1.fitness += 0.5
                genome2.fitness += 0.5
