import sys
from src.msds510.util import util


def main():
    # If the number of arguments does not equal 2 (true)
    # then we need to say that the report generator takes two
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    # if false generate report
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):
    # reading the CSV processed file
    file = util.readProcessedCSVFile(infile)
    sortedRecords = sorted(file,
                           key=lambda k: int(k['appearances']),
                           # grabbing up till number 10
                           reverse=True)[:10]

    util.printMarkdown(sortedRecords, outfile)


if __name__ == '__main__':
    main()
