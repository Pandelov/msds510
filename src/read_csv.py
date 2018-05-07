import sys
import csv                      #we import the csv module


def main():
    if (len(sys.argv) != 2):
        print("this converter takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        readCSVFile(sys.argv[1])


def readCSVFile(infile):

    with open(infile, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        print(data[161])


if __name__ == '__main__':
    main()
