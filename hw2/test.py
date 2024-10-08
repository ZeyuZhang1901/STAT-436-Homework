import numpy as np

# Generate a random 1D numpy vector that sums to 1
size = 5  # You can adjust the size as needed
random_vector = np.random.dirichlet(np.ones(size))

print("Random vector:", random_vector)
print("Sum of vector:", np.sum(random_vector))

for a, prob in enumerate(random_vector):
    print(f"Action {a}: {prob}")

