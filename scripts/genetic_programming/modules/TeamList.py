import random

import numpy as np
from modules.Parameter import Parameter
from modules.Team import Team

class TeamList:
    def __init__(self, population_list):
        self.population_list = population_list
        self.teams = self.form_teams(Parameter.individual_count)
        self.num_teams_to_remove = int(Parameter.gap_percentage * len(self.teams))

    def form_teams(self, num_teams, new_individuals_only=False):
        teams = []
        # Initialize a dictionary to keep track of the next individual to be selected from each population
        next_individual_index = {pop_label: 0 for pop_label in self.population_list.populations}

        for _ in range(num_teams):
            team_individuals = []
            for pop_label, population in self.population_list.populations.items():
                # Choose individuals based on new_individuals_only flag
                if new_individuals_only:
                    eligible_individuals = [ind for ind in population.individuals if ind.is_new]
                else:
                    eligible_individuals = population.individuals

                # Get the next individual for the team from this population
                individual = eligible_individuals[next_individual_index[pop_label]]
                team_individuals.append(individual)
                
                # Update the index for the next individual to be selected from this population
                next_individual_index[pop_label] += 1

            teams.append(Team(team_individuals))
        return teams

    def evolve(self, data, labels):
        # Step 1: Evaluate fitness for all teams (if they haven't been evaluated)
        for team in self.teams:
            if not team.fitness_evaluated:
                team.evaluate_fitness(data, labels)

        # Step 2: Apply fitness sharing adjustment (if they haven't been adjusted)
        if Parameter.fitness_sharing:
            self.fitness_sharing_adjustment(data, labels)

        # After adjusting fitness scores, mark each unevaluated team as evaluated
        for team in self.teams:
            team.fitness_evaluated = True

        # Step 3: Sort teams by fitness in descending order
        self.teams.sort(key=lambda team: team.fitness, reverse=True)

        # Determine the number of teams to keep based on gap percentage
        num_teams_to_keep = len(self.teams) - self.num_teams_to_remove

        # Step 4: Preserve the best performing teams as champions
        champions = self.teams[:num_teams_to_keep]

        # Step 5: Remove the worst-performing teams and their individuals from populations
        for team in self.teams[num_teams_to_keep:]:
            self.remove_individuals_from_populations(team)

        # Clear the team list and refill it with champions for now
        self.teams = champions

        # Step 6: Generate new children in each population
        self.population_list.generate_children()

        # Step 7: Form new teams with the new children
        new_teams = self.form_teams(self.num_teams_to_remove, new_individuals_only=True)

        # Step 8: Combine champion teams with new teams to form the new team list
        self.teams += new_teams


    def remove_individuals_from_populations(self, team):
        for ind in team.individuals:
            # Correct method name: remove_individuals
            self.population_list.populations[ind.population_label].remove_individuals([ind])


    def fitness_sharing_adjustment(self, data, actual_labels):
        num_instances = data.shape[0]  # Assuming 'data' is a 2D numpy array
        
        # Only consider teams that have not been evaluated yet for adjustment
        unevaluated_teams = [team for team in self.teams if not team.fitness_evaluated]
        num_teams = len(unevaluated_teams)
        
        # Initialize a matrix to track correct predictions for each instance by each unevaluated team
        correct_predictions = np.zeros((num_teams, num_instances))
        
        # Fill the matrix with correct predictions
        for i, team in enumerate(unevaluated_teams):
            correct_predictions[i, :] = (team.predicted_labels == actual_labels)
        
        # Iterate through each instance to adjust fitness scores based on the shared fitness concept
        for k in range(num_instances):
            # Calculate the total number of correct predictions for instance k by all unevaluated teams
            total_correct_for_instance = np.sum(correct_predictions[:, k])
            
            # Recalculate fitness scores for each team based on the adjusted contributions for this instance
            for i, team in enumerate(unevaluated_teams):
                if correct_predictions[i, k]:
                    # Calculate the adjustment for a correct prediction
                    if total_correct_for_instance > 0:
                        adjustment = 1.0 / total_correct_for_instance
                    else:
                        adjustment = 1  # If no team got it right, default to 1
                    
                    # Apply the adjustment to the team's fitness score for this instance
                    team.fitness += adjustment  # This adds the adjusted value directly to the team's fitness
