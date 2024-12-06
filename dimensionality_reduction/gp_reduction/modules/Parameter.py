from dataclasses import dataclass


@dataclass
class Parameter:
    # Number of Individuals in the Population
    individual_count = 100

    # Max Instruction (Row) per each Individual
    operation_count = 5

    # Percentage of worst fit Individuals to replace
    gap_percentage = 0.8

    # Generation Count
    generations = 10000

    # Probability of a Mutation
    mutation_prob = 0.5

    # Number of Populations (Equal to the Unique Target Labels in the Dataset)
    population_count = 2

    # Generation interval for resampling the dataset
    resample_interval = 100

    # Total instances to equally sample from the dataset's uniuqe target labels 
    sample_count = 10000

    # Tweak Fitness Sharing
    fitness_sharing = True