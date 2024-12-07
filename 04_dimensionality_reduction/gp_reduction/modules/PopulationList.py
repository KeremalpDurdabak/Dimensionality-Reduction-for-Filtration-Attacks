from modules.Parameter import Parameter
from modules.Population import Population
from modules.Dataset import Dataset

class PopulationList:
    def __init__(self):
        # Create a dictionary to hold populations, each keyed by its target label
        self.populations = {label: Population(label) for label in range(Parameter.population_count)}

    def remove_individuals(self, individuals_to_remove):
        # Remove individuals from their respective populations
        for population_label, individuals in individuals_to_remove.items():
            self.populations[population_label].remove_individuals(individuals)

    def generate_children(self):
        # For each population, generate children to fill the gap left by removed individuals
        for population in self.populations.values():
            population.generate_children()

# Add any additional methods that are necessary for the PopulationList class to function.
