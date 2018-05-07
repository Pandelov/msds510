import sys
from src.msds510.util import util


def main():
    if (len(sys.argv) != 3):
        print("this converter takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        processFile(sys.argv[1], sys.argv[2])


def processFile(infile, outfile):
    file = util.readCSVFile(infile)
    fieldnames = util.readFieldNames(infile)
    file = util.cleanFieldNames(file)
    fieldnames.append("month_joinded")

    util.writeCSVFile(outfile, file, fieldnames)


if __name__ == '__main__':                            #calling the function
    main()
