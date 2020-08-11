import glob
import os


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
    except (OSError, IOError):
        print(f'File: {os.path.join(os.path.abspath(path))} not found.')
        lines = []

    return lines


print(get_filenames('sample-es6/src'))

filenames = get_filenames('sample-es6/src')
read_file('error')
lines = read_file(filenames[0])

for line in lines:
    print(line)
