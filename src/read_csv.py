import sys
# we import the csv module
import csv


def main():
    # if there is more than one argument, then we need to say that
    # the converter takes one parameter as an input file
    if (len(sys.argv) != 2):
        print("this converter takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        # if false read csv file
        readCSVFile(sys.argv[1])


def readCSVFile(infile):

    with open(infile, 'rU') as csvfile:
        # read the csv file in a much nicer format
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        print(data[161])


if __name__ == '__main__':
    main()
