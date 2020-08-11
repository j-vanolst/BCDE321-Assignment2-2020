class File:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.classes = []

    def add_class(self, newClass):
        self.classes.append(newClass)

    def __str__(self):
        for aClass in self.classes:
            print(
                f'Classes: {aClass.name} Attributes: {aClass.attributes} Methods: {len(aClass.methods)}')
        return f'Filename: {self.name}\nLocation: {self.location}'
