import glob
import os

def get_filenames(path):
    filenames = []

    for folder in os.walk(path):
        for filename in glob.glob(os.path.join(folder[0], '*.js')):
            filenames.append(filename)

    return filenames

print(get_filenames('sample-es6/src'))

