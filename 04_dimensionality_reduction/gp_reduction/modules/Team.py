import numpy as np

class Team:
    def __init__(self, individuals):
        self.individuals = individuals
        self.fitness = 0
        self.fitness_evaluated = False  # Indicates both fitness calculated and adjusted
        self.individual_to_population = {ind: ind.population_label for ind in individuals}
        self.predicted_labels = []

    def evaluate_fitness(self, data, actual_labels):
        # Vectorized evaluation of all individuals for all instances
        evaluations = np.array([individual.evaluate(data) for individual in self.individuals])

        # Find the index of the best performing individual for each instance
        winning_indices = np.argmax(evaluations, axis=0)

        # Map the winning indices to population labels
        population_labels = np.array([ind.population_label for ind in self.individuals])
        self.predicted_labels = population_labels[winning_indices]

        # Count the number of correct predictions
        correct_predictions = self.predicted_labels == actual_labels
        self.fitness = np.sum(correct_predictions)