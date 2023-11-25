# Custom exception classes and error handling utilities

class BrainSimulationError(Exception):
    """Base class for exceptions in the BrainSimulationProject."""
    pass

class DataImportError(BrainSimulationError):
    """Exception raised for errors in data import process."""
    def __init__(self, message="Error occurred while importing data"):
        self.message = message
        super().__init__(self.message)

class ModelInitializationError(BrainSimulationError):
    """Exception raised for errors during model initialization."""
    def __init__(self, message="Model initialization failed"):
        self.message = message
        super().__init__(self.message)

class SimulationError(BrainSimulationError):
    """Exception raised for errors encountered during simulations."""
    def __init__(self, message="Error occurred during simulation"):
        self.message = message
        super().__init__(self.message)

class ParameterValueError(BrainSimulationError):
    """Exception raised for invalid parameter values."""
    def __init__(self, parameter, message=None):
        self.parameter = parameter
        if message is None:
            self.message = f"Invalid value for parameter: {parameter}"
        else:
            self.message = message
        super().__init__(self.message)

class ComputationalLimitError(BrainSimulationError):
    """Exception raised when computational limits are exceeded."""
    def __init__(self, message="Computational limit exceeded"):
        self.message = message
        super().__init__(self.message)

class NetworkTopologyError(BrainSimulationError):
    """Exception raised for errors related to network topology."""
    def __init__(self, message="Network topology error"):
        self.message = message
        super().__init__(self.message)

class DataValidationError(BrainSimulationError):
    """Exception raised for errors in data validation."""
    def __init__(self, message="Data validation failed"):
        self.message = message
        super().__init__(self.message)

# Additional custom exceptions can be defined here as needed

def handle_exception(e):
    """Generic exception handling function."""
    # Here you can add logging or more sophisticated exception handling
    print(f"An error occurred: {str(e)}")
