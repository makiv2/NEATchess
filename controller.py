from chesstrainer import train_ai


def evaluate_population(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 50
        for genome_id2, genome2 in genomes[i + 1:]:
            genome2.fitness = 50 if genome2.fitness is None else genome2.fitness
            # Train two and two genomes against each other
            train_ai(genome1, genome2, config)






