from struct import *
import os

imgdir = '/Users/dragonjohn/Documents/DevEnv/Trend/digit/test/'
imgdir2 = '/Users/dragonjohn/Documents/DevEnv/Trend/digit/digit-test-new/test-new/'

#list = []
csvfile = 'testR1_more10000.csv'
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


for file in os.listdir(imgdir2):
    content = []
    content.append(file)

    f= open(imgdir2+file, 'rb')
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
