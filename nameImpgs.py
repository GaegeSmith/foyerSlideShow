from useful import *

from os import listdir
from os.path import isfile, join
onlyfiles = []

print(Terminal.filePath() + "imgsToAdd\\")

for f in listdir(Terminal.filePath() + "imgsToAdd\\"):
    onlyfiles.append(f)

for f in onlyfiles:
    print(f)


# get a list of all filenames