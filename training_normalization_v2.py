from struct import *
import os
import csv

inputfilepath = '/Users/dragonjohn/Documents/DevEnv/Python/MLCR1digitRecog/training_augmented_20160418.csv'

outputcsvfile = 'trainR1_more_v2.csv'
outputfile = open(outputcsvfile, 'w')

with open(inputfilepath) as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        content = []
        content.append(str(int(float(row[1]))))
        content+=map(lambda x:str(int(round(float(x)*255))), row[2:])
        #print content
        outputfile.write(",".join(content)+os.linesep)
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
