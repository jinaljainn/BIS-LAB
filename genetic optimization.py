
import random
import math

# Fitness function
def fitness(angle):
    return 100 * math.sin(math.radians(angle + 10))

# Initial population
population = [random.uniform(0, 90) for _ in range(10)]

# Genetic Algorithm
for generation in range(50):
    population.sort(key=fitness, reverse=True)

    # Selection
    parents = population[:5]

    # Crossover
    children = [(parents[i] + parents[i+1]) / 2
                for i in range(4)]

    # Mutation
    for i in range(len(children)):
        if random.random() < 0.2:
            children[i] += random.uniform(-5, 5)

        children[i] = max(0, min(90, children[i]))

    population = parents + children

# Best solution
best = max(population, key=fitness)

print("Best Tilt Angle:", round(best, 2), "degrees")
print("Maximum Fitness:", round(fitness(best), 2))
