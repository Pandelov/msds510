import sys
from src.msds510.util import util


def main():
    if (len(sys.argv) != 3):                            #If the number of arguments does not equal 2 (true)
        print("this converter takes two parameters, "   #then we need to say that the converter takes two parameters
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])             #if false process the file
        print("output file: " + sys.argv[2])
        processFile(sys.argv[1], sys.argv[2])


def processFile(infile, outfile):                       #defining a function called processFile. It has two parameters.
    file = util.readCSVFile(infile)                     #reading the csv file
    fieldnames = util.readFieldNames(infile)
    file = util.cleanFieldNames(file)                   #cleaning the file
    fieldnames.append("month_joinded")

    util.writeCSVFile(outfile, file, fieldnames)


if __name__ == '__main__':                            #calling the function
    main()
