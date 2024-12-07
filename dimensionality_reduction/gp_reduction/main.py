from modules.Dataset import Dataset
from modules.Parameter import Parameter
from modules.PopulationList import PopulationList
from modules.TeamList import TeamList
from modules.Display import Display

import os

def main():
    num_runs = 1  # Number of runs for each dataset

    for run in range(1, num_runs + 1):

        # Create a new directory for each run
        run_directory = f'Lorem/Ipsum/Fitness_Sharing/FS_RUN{run}'
        os.makedirs(run_directory, exist_ok=True)

        # File paths for saving results
        fitness_save_path = f'{run_directory}/unb2017_best_fitness_scores.txt'
        equation_save_path = f'{run_directory}/unb2017_eq.txt'

        # Load training dataset
        train_path = r"Lorem\Ipsum\SESSION_Original_Stratified_Train.csv"
        
        Dataset.load_dataset(train_path)
        Dataset.stratified_sample(Parameter.sample_count)
        
        populationList = PopulationList()
 
        print('Forming Teams...')
        teamList = TeamList(populationList)

        best_fitness_scores = []
        latest_equation = ''

        for generation in range(1, Parameter.generations + 1):
            if generation % Parameter.resample_interval == 1:  # Resample at specified intervals
                Dataset.stratified_sample(Parameter.sample_count)

            print(f'Generation: {generation}')
            teamList.evolve(Dataset.X_train.values, Dataset.y_train.values)
            
            best_team = teamList.teams[0]
            best_fitness_scores.append(best_team.fitness)
            latest_equation = Display.generationReport(best_team)

        Display.overallReport(best_fitness_scores)

        # Write the best fitness scores to a text file
        with open(fitness_save_path, 'w') as file:
            for score in best_fitness_scores:
                file.write(f"{score}\n")

        # Write the latest equation to a text file
        with open(equation_save_path, 'w') as file:
            file.write(f"{latest_equation}\n")

if __name__ == '__main__':
    main()