import random
import time
from typing import List, Callable, Iterable, Tuple

Gene = List[int]


def small_random_probability() -> bool:
    """Returns True only very small number of times"""
    return random.random() < 0.01


def best_individual(population: List[Gene], fitness: Callable[[Gene], float]) -> Gene:
    return max(zip(population, map(fitness, population)), key=lambda x: x[1])[0]


def reproduce(parent1: Gene, parent2: Gene) -> Gene:
    n = len(parent1)
    c = random.randint(1, n - 1)
    return parent1[:c] + parent2[c:]


def mutate(person: Gene) -> Gene:
    n = len(person)
    # flip any 2 random bits
    for _ in range(2):
        i = random.randint(0, n - 1)
        person[i] = random.randint(1, n)
    return person


def select_parents(population: List[Gene], weights: List[float]) -> Tuple[Gene, Gene]:
    parent1 = random.choices(population, weights=weights, k=1)[0]
    parent2 = random.choices(population, weights=weights, k=1)[0]
    return parent1, parent2


def genetic_algorithm(population: List[Gene], fitness: Callable[[Gene], float], max_time: int) -> Gene:
    start_time = time.time()
    while fitness(best_individual(population, fitness)) < 1 and (time.time() - start_time < max_time):
        weights: List[float] = list(map(fitness, population))
        population2: List[Gene] = []
        for i in range(len(weights)):
            parent1, parent2 = select_parents(population, weights)
            child = reproduce(parent1, parent2)
            if small_random_probability():
                child = mutate(child)
            population2.append(child)
        population = population2
    return best_individual(population, fitness)


def get_seed_population(size: int, n_queens: int) -> Iterable[Gene]:
    for _ in range(size):
        # Form a gene
        gene: Gene = [random.randint(1, n_queens) for _ in range(n_queens)]
        yield gene


def n_queen_fitness(gene: Gene) -> float:
    n = len(gene)
    attacking_pairs = sum(
        gene[i] == gene[j] or abs(gene[i] - gene[j]) == abs(i - j)
        for i in range(n) for j in range(i + 1, n)
    )
    total_n_pairs = (n * (n - 1)) << 1
    return attacking_pairs / total_n_pairs


def main():
    n_queens = 8
    population_size = 1000
    initial_population = list(get_seed_population(population_size, n_queens))
    best_config = genetic_algorithm(initial_population, n_queen_fitness, max_time=10)
    print(best_config, n_queen_fitness(best_config))


if __name__ == '__main__':
    main()
