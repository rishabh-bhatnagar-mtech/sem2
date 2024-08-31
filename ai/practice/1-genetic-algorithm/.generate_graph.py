import os

import matplotlib.pyplot as plt
import numpy as np

from n_queens import get_seed_population, genetic_algorithm, n_queen_fitness

# Define the ranges for max_time and max_n_epochs
MAX_TIME_RANGE = np.linspace(1, 20, 5)  # 20 values between 1 and 20
MAX_N_EPOCHS_RANGE = np.logspace(
    np.log10(10), np.log10(10000), num=5
)  # 20 values from 10 to 10000

# File path for caching results
CACHE_FILE = 'results_cache.npy'

# Genetic algorithm params:
population_size = 1000
n_queens = 8

# Check if cached results exist
if os.path.exists(CACHE_FILE):
    print("Loading cached results...")
    scores = np.load(CACHE_FILE)
else:
    # Initialize arrays to store results
    scores = np.zeros((len(MAX_TIME_RANGE), len(MAX_N_EPOCHS_RANGE)))

    # Compute scores for each combination of max_time and max_n_epochs
    initial_population = list(get_seed_population(population_size, n_queens))
    for i, max_time in enumerate(MAX_TIME_RANGE):
        for j, max_n_epochs in enumerate(MAX_N_EPOCHS_RANGE):
            best_config = genetic_algorithm(
                initial_population, n_queen_fitness,
                max_time=max_time, max_n_epochs=int(max_n_epochs)
            )
            scores[i, j] = n_queen_fitness(best_config)

    # Save the results to a file
    print("Saving results to cache...")
    np.save(CACHE_FILE, scores)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(MAX_N_EPOCHS_RANGE, MAX_TIME_RANGE)
Z = scores

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Labels and title
ax.set_xlabel('# Generations')
ax.set_ylabel('Time')
ax.set_zlabel('Score')
ax.set_title('3D Surface Plot of Genetic Algorithm Performance')

plt.show()
