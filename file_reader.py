import os
import re
import glob

from model.file import File

filename_regex = '(?<=[a-zA-Z0-9])*[a-zA-Z0-9]+\.[a-zA-Z0-9]*'

def get_filenames(path):
    '''Returns a list of all javascript files recursively from a given path'''
    filenames = []

    for folder in os.walk(path):
        for filename in glob.glob(os.path.join(folder[0], '*.js')):
            filenames.append(filename)

    return filenames

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


filenames = get_filenames('sample-es6/src')
files = []

for filename in filenames:
    file_read = read_file(filename)
    new_file = File(file_read[0], file_read[1], file_read[2])
    files.append(new_file)

for file in files:
    print(file)

# file = read_file('sample-es6/src/js/html.js')
# file = read_file('test2.js')
# new_file = File(file[0], file[1], file[2])
# print(new_file)
