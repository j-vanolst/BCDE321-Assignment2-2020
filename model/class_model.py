class Class:
    def __init__(self, name):
        self.name = name
        self.methods = []
        self.attributes = []

    def add_method(self, newMethod):
        self.methods.append(newMethod)

    def add_attribute(self, newAttribute):
        self.attributes.append(newAttribute)
