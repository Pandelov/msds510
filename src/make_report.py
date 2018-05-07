import sys
from src.msds510.util import util

def main():

    if len(sys.argv) != 3:                                      #If the number of arguments does not equal 2 (true)
        print("this report generator takes two parameters, "    #then we need to say that the converter takes two parameters
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])                     #if false generate report
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):

    file = util.readProcessedCSVFile(infile)                    #reading the CSV processed file
    sortedRecords = sorted(file,
                           key=lambda k: int(k['appearances']),
                           reverse=True)[:10]                               #grabbing up till number 10

    util.printMarkdown(sortedRecords, outfile)


if __name__ == '__main__':
    main()
