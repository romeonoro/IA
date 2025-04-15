import random
from util import Util

class Chromosome:

    def __init__(self, city, target_state):
        self.city = city
        self.fitness = self.calculate_fitness(target_state)

    # Heuristic function to calculate fitness based on disorder and duplicates
    def calculate_fitness(self, target_state):
        penalty = 0

        # Penalty for incorrect order
        for i in range(len(target_state) - 1):
            if self.city[i] > self.city[i+1]:
                penalty += 10

        # Count occurrences of each digit
        count = {}
        for c in self.city:
            count[c] = count.get(c, 0) + 1

        # Penalty for repeated digits
        for qty in count.values():
            if qty > 1:
                pairs = (qty * (qty - 1)) // 2
                penalty += pairs * 20

        return penalty

    def __str__(self):
        return f'{self.city} - {self.fitness}'

    def __eq__(self, other):
        if isinstance(other, Chromosome):
            return self.city == other.city
        return False

    @staticmethod
    def generate_population(population, quantity, target_state):
        for _ in range(quantity):
            new_city = Util.generate_city(len(target_state))
            individual = Chromosome(new_city, target_state)
            population.append(individual)

    @staticmethod
    def show_population(population, generation):
        print(f'Generation {generation}')
        for individual in population:
            print(individual)

    @staticmethod
    def tournament_selection(population, new_population, selection_rate):
        num_selected = int(len(population) * selection_rate / 100)
        tournament = []

        # Elitism: keep the best individual
        new_population.append(population[0])


        i = 1
        while i < num_selected:
            s1 = population[random.randrange(len(population))]

            while True:
                s2 = population[random.randrange(len(population))]
                if s2 != s1:
                    break

            while True:
                s3 = population[random.randrange(len(population))]
                if s3 != s1 and s3 != s2:
                    break

            tournament.extend([s1, s2, s3])
            tournament.sort(key=lambda chrom: chrom.fitness)

            if tournament[0] not in new_population:
                new_population.append(tournament[0])
                i += 1

            tournament.clear()


   @staticmethod
    def reproduce(population, new_population, reproduction_rate, target_state):
        num_to_reproduce = int(len(population) * reproduction_rate / 100)

        for _ in range((num_to_reproduce // 2) + 1):
            parent1 = population[random.randrange(len(population))]

            while True:
                parent2 = population[random.randrange(len(population))]
                if parent2 != parent1:
                    break

            city1 = parent1.city
            city2 = parent2.city

            half1 = city1[:len(city1)//2]
            half2 = city2[len(city2)//2:]
            half3 = city2[:len(city2)//2]
            half4 = city1[len(city1)//2:]

            child1 = half1 + half2
            child2 = half3 + half4

            new_population.append(Chromosome(child1, target_state))
            new_population.append(Chromosome(child2, target_state))

            # Remove excess individuals
            while len(new_population) > len(population):
                new_population.pop()

    @staticmethod
    def mutate(population, target_state):
        num_mutants = random.randrange(1, max(2, int(len(population) / 5)))

        while num_mutants > 0:
            mutant_index = random.randrange(len(population))
            mutant = population[mutant_index]
            print('\nMutating...', mutant)

            city = mutant.city
            char_to_mutate = city[random.randrange(len(city))]
            new_char = Util.digits[random.randrange(Util.size)]

            new_city = city.replace(char_to_mutate, new_char)

            new_mutant = Chromosome(new_city, target_state)
            population[mutant_index] = new_mutant
            num_mutants -= 1
