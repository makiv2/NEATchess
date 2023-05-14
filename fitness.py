from chesstrainer import train_ai


def evaluate_population(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i + 1]:
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            # Initialize game
            train_ai(genome1, genome2, config)


def calculate_fitness(genome1, genome2, game_info):
    pass
