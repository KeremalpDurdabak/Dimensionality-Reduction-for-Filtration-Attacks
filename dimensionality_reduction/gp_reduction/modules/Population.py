from modules.Dataset import Dataset
from modules.Individual import Individual
from modules.OperationSet import OperationSet
from modules.Parameter import Parameter
import random
import numpy as np

class Population:
    def __init__(self, label):
        self.label = label
        self.individuals = [Individual(label) for _ in range(Parameter.individual_count)]

    def remove_individuals(self, individuals_to_remove):
        self.individuals = [ind for ind in self.individuals if ind not in individuals_to_remove]

    def generate_children(self):
        num_children = int(Parameter.individual_count * Parameter.gap_percentage)
        children = self.crossover_and_mutate(num_children)
        for child in children:
            child.is_new = True
        self.individuals.extend(children)

    def crossover_and_mutate(self, num_children):
        children = []
        while len(children) < num_children:
            if len(self.individuals) < 2:
                raise Exception("Not enough parents for crossover")
            parents = random.sample(self.individuals, 2)

            if random.random() < 0.5:
                child1, child2 = self.single_point_crossover(parents[0], parents[1])
            else:
                child1, child2 = self.double_point_crossover(parents[0], parents[1])

            self.mutate(child1)
            self.mutate(child2)

            children.extend([child1, child2])

        return children[:num_children]

    def single_point_crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.equation) - 1)
        child1_equation = parent1.equation[:crossover_point] + parent2.equation[crossover_point:]
        child2_equation = parent2.equation[:crossover_point] + parent1.equation[crossover_point:]
        return Individual(self.label).with_equation(child1_equation), Individual(self.label).with_equation(child2_equation)

    def double_point_crossover(self, parent1, parent2):
        crossover_points = sorted(random.sample(range(1, len(parent1.equation)), 2))
        child1_equation = (parent1.equation[:crossover_points[0]] + parent2.equation[crossover_points[0]:crossover_points[1]] + parent1.equation[crossover_points[1]:])
        child2_equation = (parent2.equation[:crossover_points[0]] + parent1.equation[crossover_points[0]:crossover_points[1]] + parent2.equation[crossover_points[1]:])
        return Individual(self.label).with_equation(child1_equation), Individual(self.label).with_equation(child2_equation)

    def mutate(self, individual):
        for i in range(len(individual.equation)):
            if random.random() < Parameter.mutation_prob:
                # Mutate operation with 50% probability
                if random.random() < 0.5:
                    operation, _ = OperationSet.get_random_operation()
                    # Keep the original operands, but update the operation
                    individual.equation[i] = (operation, individual.equation[i][1])
                else:
                    # Mutate operands
                    # For 'add' and 'subtract', choose two random operands from the features
                    if individual.equation[i][0] in ['add', 'subtract']:
                        operands = random.sample(range(Dataset.feature_count), 2)
                    else:  # For 'multiply' and 'divide', set the second operand to 2 explicitly
                        first_operand = random.choice(range(Dataset.feature_count))
                        operands = [first_operand, 2]
                    # Update the equation with possibly new operation and new operands
                    individual.equation[i] = (individual.equation[i][0], operands)
                individual.evaluated = False
