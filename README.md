**Problem Statement:**
The Knapsack Problem is a classic optimization problem where the objective is to select a subset of
items, each with a given weight and value, to maximize the total value while staying within a given
weight constraint. Formally, given a set of items with weights wi​ and values vi​, and a knapsack of
capacity W, the goal is to find the subset of items that maximizes the total value without exceeding the
knapsack capacity.

**Genetic Algorithm Parameters:**

**1. Chromosome Representation:**
Each chromosome represents a potential solution and is encoded as a binary string of
length N, where N is the number of items. The presence of a gene at position i indicates
whether the corresponding item is selected (1) or not (0).

**2. Initialization:**
Generate an initial population of potential solutions (chromosomes) randomly.

**3. Fitness Function:**
Define the fitness function to evaluate the quality of each chromosome. The fitness
score is calculated as the total value of the selected items in the knapsack. If the total
weight exceeds the knapsack capacity, assign a fitness score of 0.

**4. Crossover Policy:**
Use a two-point crossover policy to create offspring. Randomly select two crossover
points on both parent chromosomes and exchange the genetic material between these
points to produce two offspring.

**5. Mutation Operation:**
Implement a mutation operation to introduce genetic diversity. Randomly select a gene
in a chromosome and flip its value with a certain probability. This simulates the
introduction of new genetic material into the population.

**6. Selection Strategy:**
Employ a selection strategy, such as tournament selection, to choose parents for
crossover based on their fitness scores. This helps to bias the selection towards fitter
individuals.
**7. Termination Criteria:**
Define termination criteria for the genetic algorithm, such as a maximum number of
generations or achieving a certain fitness threshold.
