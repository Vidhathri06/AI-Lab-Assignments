import random
POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Vidhathri"

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        return [cls.mutated_genes() for _ in range(len(TARGET))]

    def mate(self, partner):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)  
            elif prob < 0.90:
                child_chromosome.append(gp2)  
            else:
                child_chromosome.append(self.mutated_genes())  
        return Individual(child_chromosome)

    def cal_fitness(self):
        return sum(1 for gs, gt in zip(self.chromosome, TARGET) if gs != gt)

def initialize_population():
    return [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

def select_parents(population):
    return random.sample(population, 2)

def main():
    generation = 1
    found = False
    population = initialize_population()
    while not found:
        population = sorted(population, key=lambda x: x.fitness)
        if population[0].fitness == 0:
            found = True
            break
        new_generation = []
        new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])
        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1, parent2 = select_parents(population)
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation
        print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")
        generation += 1
    print(f"Generation: {generation}\tString: {''.join(population[0].chromosome)}\tFitness: {population[0].fitness}")

if __name__ == '__main__':
    main()
