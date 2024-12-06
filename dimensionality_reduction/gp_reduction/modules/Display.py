import matplotlib.pyplot as plt

from modules.Parameter import Parameter

class Display:
    @staticmethod
    def generationReport(team):
        #print(f"Highest Fitness Team: {(team.fitness/Parameter.sample_count)*100}%")
        print(f"Champion Team Fitness: {team.fitness}")
        #print(f"Champion Team Adjusted Fitness: {team.adjusted_fitness}")
        current_equation = []
        for individual in team.individuals:
            # Assuming individual.population_label indicates the target label the individual is predicting
            current_equation_str = f"Prediction for class '{individual.population_label}': {individual}"
            current_equation.append(current_equation_str)
            print(current_equation_str)
        return '\n'.join(current_equation)


    @staticmethod
    def overallReport(fitness_over_generations):
        plt.plot(fitness_over_generations)
        plt.xlabel('Generation')
        plt.ylabel('Best Fitness Score')
        plt.title('Fitness Score Over Generations')
        plt.savefig('fitness_over_generations.png')
        #plt.show()
