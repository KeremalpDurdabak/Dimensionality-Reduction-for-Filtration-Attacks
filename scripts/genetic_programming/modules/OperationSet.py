import random
import numpy as np


class OperationSet:
    # Define the operation pool with NumPy operations
    OPERATIONS = {
        'add': np.add,
        'subtract': np.subtract,
        'multiply': np.multiply,  # Use the built-in NumPy multiply function
        'divide': np.divide  # Use the built-in NumPy divide function
    }

    @staticmethod
    def get_random_operation():
        # Randomly select an operation
        operation = random.choice(list(OperationSet.OPERATIONS.keys()))
        return operation, OperationSet.OPERATIONS[operation]
