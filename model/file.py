import re

from model.class_model import Class

class_regex = '(?<=class\s)[a-zA-Z0-9]+((?:extends)?\s[a-zA-Z0-9]+)*(?=\s\{)'


class File:
    '''Represents a file object, contains a filename, location, file lines and a list of classes'''
    def __init__(self, name, location, lines):
        self.name = name
        self.location = location
        self.lines = lines
        self.classes = []

        self.find_classes()

    def add_class(self, newClass):
        self.classes.append(newClass)

    def find_classes(self):
        '''Uses regular expressions to locate class definitions within a JavaScript file'''
        for aLine in self.lines:
            re_match = re.search(class_regex, aLine)
            if (re_match):
                newClass = Class(re_match.group(), self.lines)
                self.add_class(newClass)

    def __str__(self):
        output_string = '\n'
        output_string += f'Filename: {self.name}\n'
        output_string += f'Location: {self.location}\n'

        output_string += f'{len(self.classes)} Class(es):\n'
        for aClass in self.classes:
            output_string += str(aClass)

        return output_string
