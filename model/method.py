class Method:
    def __init__(self, name):
        self.name = name
        self.parameters = []

    def add_parameter(self, newParameter):
        self.parameters.append(newParameter)
