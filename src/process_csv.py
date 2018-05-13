import sys
from src.msds510.util import util


def main():
    # If the number of arguments does not equal 2 (true)
    # then we need to say that the converter takes two parameters
    if (len(sys.argv) != 3):
        print("this converter takes two parameters, "
              "an input file and an output file")
    # if false process the file
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        processFile(sys.argv[1], sys.argv[2])


# defining a function called processFile. It has two parameters.
def processFile(infile, outfile):
    # reading the csv file
    file = util.readCSVFile(infile)
    fieldnames = util.readFieldNames(infile)
    # cleaning the file
    file = util.cleanFieldNames(file)
    fieldnames.append("month_joinded")

    util.writeCSVFile(outfile, file, fieldnames)


# calling the function
if __name__ == '__main__':
    main()
