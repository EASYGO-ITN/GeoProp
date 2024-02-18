class Error(Exception):
    pass


class InputError(Error):

    def __init__(self, message):
        self.message = message


class ConvergenceError(Error):

    def __init__(self, message):
        self.message = message


class CalculationError(Error):

    def __init__(self, message):
        self.message = message