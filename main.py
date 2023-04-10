from m4atowav import format_converter
import math
import os
from dft import SpectrumAnalyzer

# Folder Paths containing recording in m4a format
path = ["Jason/", "Ruchit/", "Rifa/", "Karina/"]
# convert to wav
for i in path:
    format_converter(i)

for i in path:
    for (dirpath, dirnames, filenames) in os.walk(i):
        res = [i+j for i,j in zip(path,filenames)]

if __name__ == "__main__":
    dft = SpectrumAnalyzer()
    for j in res:
        max_freq = dft.graphResults(j)
