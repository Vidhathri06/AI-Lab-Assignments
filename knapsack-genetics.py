import random
knapsack_capacity=50
weights=[10,20,30,40,50]
values=[60,100,120,150,200]
population_size=50
generations=100
mutation_rate=0.1
tournament_size=5

def generate_chromosome():
    return [random.choice([0, 1]) for _ in range(len(weights))]

def initialize_population():
    return [generate_chromosome() for _ in range(population_size)]

def calculate_fitness(chromosome):
    total_value=sum(c*v for c,v in zip(chromosome,values))
    total_weight=sum(c*w for c,w in zip(chromosome,weights))
    return total_value if total_weight <= knapsack_capacity else 0

def tournament_selection(population):
    selected=random.sample(population,tournament_size)
    return max(selected,key=calculate_fitness)

def select_parents(population):
    return [tournament_selection(population) for _ in range(population_size)]

def two_point_crossover(parent1,parent2):
    point1,point2=sorted(random.sample(range(len(parent1)),2))
    child1=parent1[:point1]+parent2[point1:point2]+parent1[point2:]
    child2=parent2[:point1]+parent1[point1:point2]+parent2[point2:]
    return child1,child2

def mutate(chromosome):
    mutation_point=random.randint(0,len(chromosome)-1)
    chromosome[mutation_point]=1-chromosome[mutation_point]

def apply_mutation(population):
    for chromosome in population:
        if random.random()<mutation_rate:
            mutate(chromosome)

def genetic_algorithm():
    population=initialize_population()
    for _ in range(generations):
        parents=select_parents(population)
        offspring=[]
        for i in range(0,len(parents),2):
            if i+1<len(parents):
                child1,child2=two_point_crossover(parents[i],parents[i+1])
                offspring.extend([child1,child2])
        apply_mutation(offspring)
        population=offspring
    best_solution=max(population,key=calculate_fitness)
    return best_solution,calculate_fitness(best_solution)

best_solution,best_fitness=genetic_algorithm()
print("Best Solution (Selected items):",best_solution)
print("Best Fitness (Total value):",best_fitness)

