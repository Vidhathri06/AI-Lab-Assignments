import random
import numpy as np
NUM_ITEMS = 10
BIN_CAPACITY = 15
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
NUM_GENERATIONS = 100
ITEM_SIZES=[random.randint(1,10) for _ in range(NUM_ITEMS)]

def generate_chromosome():
    return [random.randint(0,NUM_ITEMS-1) for _ in range(NUM_ITEMS)]

def initialize_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    bins={}
    for item,bin_id in enumerate(chromosome):
        if bin_id not in bins:
            bins[bin_id]=0
        bins[bin_id]+=ITEM_SIZES[item]
    overfilled_penalty=sum(max(0, bins[b]-BIN_CAPACITY) for b in bins)
    return len(bins)+overfilled_penalty  

def selection(population):
    selected=random.sample(population,3)
    return min(selected,key=fitness)

def crossover(parent1,parent2):
    point=random.randint(1,NUM_ITEMS-1)
    child1=parent1[:point]+parent2[point:]
    child2=parent2[:point]+parent1[point:]
    return child1,child2

def mutate(chromosome):
    if random.random()<MUTATION_RATE:
        index=random.randint(0,NUM_ITEMS-1)
        chromosome[index]=random.randint(0,NUM_ITEMS-1)
    return chromosome

def genetic_algorithm():
    population=initialize_population()
    for generation in range(NUM_GENERATIONS):
        new_population=[]
        for _ in range(POPULATION_SIZE//2):
            parent1,parent2=selection(population),selection(population)
            child1,child2=crossover(parent1,parent2)
            new_population.extend([mutate(child1),mutate(child2)])
        population=sorted(new_population,key=fitness)[:POPULATION_SIZE]
        best_fitness=fitness(population[0])
        print(f"Generation {generation+1}, Best Fitness: {best_fitness}")
    return population[0]  
best_solution=genetic_algorithm()
print("Best Bin Packing Arrangement:",best_solution)
