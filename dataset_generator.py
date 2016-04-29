from struct import *
import os

imgdir = '/Users/dragonjohn/Documents/DevEnv/Trend/digit/train/'
#list = []
csvfile = 'trainR1_more.csv'
outputfile = open(csvfile, 'w')

for file in os.listdir(imgdir):
    content = []
    content.append(file)

    f= open(imgdir+file, 'rb')
    try:
        byte = f.read(1)
        while byte != "":
            digit = unpack('>B', byte)[0]
            content.append(str(digit))
            #print digit
            byte = f.read(1)
    finally:
        f.close()
    outputfile.write(','.join(content)+os.linesep)
outputfile.close()
#print list
