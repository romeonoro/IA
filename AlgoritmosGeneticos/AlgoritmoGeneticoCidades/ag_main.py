import random
from chromosome import Chromosome 

class Main:
    
    # Target goal state
    target_state = '123456789'

    # Read input parameters from user
    num_chromosomes = int(input('Number of chromosomes: '))
    num_generations = int(input('Number of generations: '))
    selection_rate = int(input('Selection rate [25 to 75]: '))
    mutation_rate = int(input('Mutation rate: '))
    reproduction_rate = 100 - selection_rate

    # Population initialization
    population = []
    new_population = []
    best_history = dict()  # Tracks the best fitness per generation

    # Generate initial random population
    Chromosome.generate_population(population, num_chromosomes, target_state)
    population.sort(key=lambda c: c.fitness)
    Chromosome.show_population(population, 0)
    best_history[0] = population[0].fitness

    # Main loop of the genetic algorithm
    for generation in range(1, num_generations):
        Chromosome.tournament_selection(population, new_population, selection_rate)
        Chromosome.reproduce(population, new_population, reproduction_rate, target_state)

        # Apply mutation based on probability
        if random.random() < (mutation_rate / 100):
            Chromosome.mutate(new_population, target_state)

        # Update the population
        population.clear()
        population.extend(new_population)
        new_population.clear()
        population.sort(key=lambda c: c.fitness)

        # Display current generation
        Chromosome.show_population(population, generation)
        best_history[generation] = population[0].fitness

        # Early stopping if optimal solution is found
        if population[0].fitness == 0:
            print(f"\nOptimal solution found in generation {generation}!")
            break

    # Final report
    best_generation = min(best_history, key=best_history.get)
    best_fitness = best_history[best_generation]

    print(f'Best fitness (closest to 0): {best_fitness}')

        
