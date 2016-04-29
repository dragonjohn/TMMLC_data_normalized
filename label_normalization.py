from struct import *
import os
import csv
from decimal import Decimal

inputfilepath = '/Users/dragonjohn/Documents/DevEnv/Python/digitUnpack/label_with_sn.csv'

outputcsvfile = 'label_fixed.csv'
outputfile = open(outputcsvfile, 'w')

with open(inputfilepath) as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        if "E+" in str(row[0]):
            labelArray = str(row[0]).split("E+")
            outputfile.write('{:.2f}'.format(Decimal(labelArray[0]))+"E+"+labelArray[1]+os.linesep)
        else:
            outputfile.write(str(row[0])+os.linesep)
outputfile.close()
csvfile.close()
#inputfile = open(inputfilepath, 'r')
#row = inputfile.read()
#
#for file in os.listdir(imgdir):
#    content = []
#    content.append(file)
#
#    f= open(imgdir+file, 'rb')
#    try:
#        byte = f.read(1)
#        while byte != "":
#            digit = unpack('>B', byte)[0]
#            content.append(str(digit))
#            #print digit
#            byte = f.read(1)
#    finally:
#        f.close()
#    outputfile.write(','.join(content)+os.linesep)
#outputfile.close()
##print list
