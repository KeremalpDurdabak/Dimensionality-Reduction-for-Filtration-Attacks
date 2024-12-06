import numpy as np
from modules.Dataset import Dataset
from modules.OperationSet import OperationSet
from modules.Parameter import Parameter

class Individual:
    def __init__(self, population_label):
        self.population_label = population_label
        self.equation = []
        self.result = None  # Evaluation result
        self.evaluated = False  # Flag for evaluation status
        self.is_new = True
        self.adjusted_fitness = None  # Adjusted fitness for fitness sharing

        # Initialize with a random equation
        for _ in range(Parameter.operation_count):
            operation, _ = OperationSet.get_random_operation()
            # Choose operands based on the operation
            if operation in ['multiply', 'divide']:
                # For multiply and divide, set the second operand to 2
                operands = [np.random.choice(Dataset.feature_count), 2]
            else:
                # For add and subtract, choose two random operands
                operands = np.random.choice(Dataset.feature_count, 2, replace=False)
            self.equation.append((operation, operands))

    def evaluate(self, data):
        if not self.evaluated:
            results = np.zeros(data.shape[0])

            for operation, operands in self.equation:
                op_func = OperationSet.OPERATIONS[operation]

                if operation == 'divide':
                    # For division, use 2 as the second operand with a safeguard against division by zero
                    divisor = np.where(data[:, operands[0]] == 0, 1, 2)
                    results += op_func(data[:, operands[0]], divisor)
                elif operation == 'multiply':
                    # For multiplication, directly use 2 as the second operand, with a safeguard for the first operand being 0
                    # Although multiplying by 0 is mathematically valid, this follows your specific requirement for a safeguard
                    multiplier = np.where(data[:, operands[0]] == 0, 1, 2)
                    results += op_func(data[:, operands[0]], multiplier)
                else:
                    # For add and subtract, use actual operands from the features
                    results += op_func(data[:, operands[0]], data[:, operands[1]])

            self.result = results
            self.evaluated = True
            self.is_new = False

        return self.result

    def with_equation(self, equation):
        new_individual = Individual(self.population_label)
        new_individual.equation = equation
        new_individual.evaluated = False
        new_individual.is_new = True
        return new_individual

    def __str__(self):
        equation_parts = []
        for operation, operands in self.equation:
            formatted_operation = self.format_operation(operation, operands)
            equation_parts.append(f"({formatted_operation})")
        return ' + '.join(equation_parts)

    def format_operation(self, operation, operands):
        # Use the operation symbols based on the operation type
        operation_symbol = '+' if operation == 'add' else '-' if operation == 'subtract' else '*' if operation == 'multiply' else '/'
        
        # For 'add' and 'subtract', show both operands as feature references (e.g., F0, F1)
        if operation in ['add', 'subtract']:
            return f"F{operands[0]} {operation_symbol} F{operands[1]}"
        else:
            # For 'multiply' and 'divide', show the first operand as a feature reference and the second operand as the numeric value 2
            return f"F{operands[0]} {operation_symbol} 2"

