import random

dependencies = ["numpy", "pandas", "matplotlib", "tensorflow", "scikit-learn", "requests"]

random_dependency = random.choice(dependencies)
print("Randomly selected dependency:", random_dependency)