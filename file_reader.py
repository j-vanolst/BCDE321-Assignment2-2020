import os
import re

from model.file import File

filename_regex = '(?<=[a-zA-Z0-9])*[a-zA-Z0-9]+\.[a-zA-Z0-9]*'

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


file = read_file('sample-es6/src/js/html.js')
new_file = File(file[0], file[1], file[2])
print(new_file)
