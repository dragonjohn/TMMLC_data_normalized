from struct import *
import os
import csv

inputfilepath = '/Users/dragonjohn/Documents/DevEnv/Python/digitUnpack/training_augmented.csv'

outputcsvfile = 'trainR1_more.csv'
outputfile = open(outputcsvfile, 'w')

with open(inputfilepath) as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        content = []
        if "E+" in str(row[0]):
            lebal_check = str(row[0]).split("E+")
            if int(lebal_check[1]) < 8:
                content.append(str(int(float(lebal_check[0])*10**int(lebal_check[1]))))
            else:
                content.append(row[0])
        else:
            content.append(row[0])
        content+=map(lambda x:str(float(x)*255), row[1:])
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
