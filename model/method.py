class Method:
    def __init__(self, name):
        self.name = name
        self.parameters = []

    def add_parameter(self, newParameter):
        self.parameters.append(newParameter)

    def __str__(self):
        output_string = ''
        output_string += self.name

        return output_string
