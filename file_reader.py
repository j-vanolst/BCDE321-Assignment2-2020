import os
import re

from model.file import File
from model.class_model import Class
from model.method import Method

filename_regex = '(?<=[a-zA-Z0-9])*[a-zA-Z0-9]+\.[a-zA-Z0-9]*'
class_regex = '(?<=class\s)[a-zA-Z0-9]+((?:extends)?\s[a-zA-Z0-9]+)*(?=\s\{)'
method_regex = '^\s*[a-zA-Z0-9]+(\(){1}[a-zA-Z0-9,\s]*(\)){1}(?=\s\{)'
attribute_regex = '(?<=this\.)[a-zA-Z0-9]*(?=\s=\s[a-zA-Z0-9\[\]\{\}])'

files = []


def read_file(path):
    '''Returns a list of all lines in a specified file'''
    try:
        file = open(path, 'r')
        lines = file.read().split('\n')
        file.close()
        location = os.path.join(os.path.abspath(path))
        re_match = re.search(filename_regex, path)
        filename = re_match.group()

    except (OSError, IOError):
        print(f'File: {os.path.join(os.path.abspath(path))} not found.')
        lines = []

    return (filename, location, lines)


def parse_file(filename, location, lines):
    newFile = File(filename, location)
    for aLine in lines:
        re_match = re.search(class_regex, aLine)
        if (re_match):
            newClass = Class(re_match.group())
            newFile.add_class(newClass)
    for aLine in lines:
        re_match = re.search(method_regex, aLine)
        if (re_match):
            newMethod = Method(re_match.group().strip())
            newFile.classes[0].add_method(newMethod)
    for aLine in lines:
        re_match = re.search(attribute_regex, aLine)
        if (re_match):
            newFile.classes[0].add_attribute(re_match.group())
    return newFile


file = read_file('sample-es6/src/js/main.js')
new_file = parse_file(file[0], file[1], file[2])
print(new_file)

# classes = []
# methods = []
# attributes = []

# for aLine in lines:
#     re_match = re.search(class_regex, aLine)
#     if (re_match):
#         classes.append(re_match.group())

# for aLine in lines:
#     re_match = re.search(method_regex, aLine)
#     if (re_match):
#         methods.append(re_match.group().strip())

# for aLine in lines:
#     re_match = re.search(attribute_regex, aLine)
#     if (re_match):
#         attributes.append(re_match.group())

# print(classes)
# print(methods)
# print(attributes)
