from struct import *
import os
import csv
from decimal import Decimal

inputfilepath = '/Users/dragonjohn/Documents/DevEnv/Python/digitUnpack/trainR1_more.csv'

outputcsvfile = 'train_label_fixed.csv'
outputfile = open(outputcsvfile, 'w')

with open(inputfilepath) as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        outputfile.write(str(row[0])+os.linesep)
outputfile.close()
csvfile.close()
