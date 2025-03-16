import random
import numpy as np
NUM_JOBS=6
NUM_MACHINES=3
POPULATION_SIZE=10
MUTATION_RATE=0.1
NUM_GENERATIONS=100

PROCESSING_TIMES=[random.randint(1,10) for _ in range(NUM_JOBS)]

def generate_chromosome():
    return [random.randint(0,NUM_MACHINES-1) for _ in range(NUM_JOBS)]

def initialize_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    machine_times=[0]*NUM_MACHINES
    for job,machine in enumerate(chromosome):
        machine_times[machine]+=PROCESSING_TIMES[job]
    return 1/max(machine_times)  

def selection(population):
    fitness_scores=[fitness(chrom) for chrom in population]
    total_fitness=sum(fitness_scores)
    probabilities=[f/total_fitness for f in fitness_scores]
    return population[np.random.choice(range(POPULATION_SIZE),p=probabilities)]

def crossover(parent1,parent2):
    point1,point2=sorted(random.sample(range(NUM_JOBS),2))
    child1=parent1[:point1]+parent2[point1:point2]+parent1[point2:]
    child2=parent2[:point1]+parent1[point1:point2]+parent2[point2:]
    return child1,child2

def mutate(chromosome):
    if random.random()<MUTATION_RATE:
        index=random.randint(0,NUM_JOBS-1)
        chromosome[index]=random.randint(0,NUM_MACHINES-1)
    return chromosome

def genetic_algorithm():
    population=initialize_population()
    
    for generation in range(NUM_GENERATIONS):
        new_population=[]
        for _ in range(POPULATION_SIZE//2):
            parent1,parent2=selection(population),selection(population)
            child1,child2=crossover(parent1,parent2)
            new_population.extend([mutate(child1),mutate(child2)])
        population=sorted(new_population,key=fitness,reverse=True)[:POPULATION_SIZE]
        best_fitness=fitness(population[0])
        print(f"Generation {generation+1},Best Fitness: {best_fitness:.5f}")
    
    return population[0]  
best_schedule=genetic_algorithm()
print("Best Schedule Found:",best_schedule)