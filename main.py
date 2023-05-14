# This is a sample Python script.
import os.path

import neat
import chess

from const import *
from fitness import evaluate_population


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    # Run for up to 300 generations.
    winner = p.run(evaluate_population, GENERATIONS)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(evaluate_population, 10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    run(config_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
