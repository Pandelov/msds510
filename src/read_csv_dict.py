import sys
import csv                                                 # import the csv module


def main():                                                # if there is more than one argument, then we need to say that
    if (len(sys.argv) != 2):                               # the converter takes one parameter as an input file
        print("this converter takes one parameters, "
              "an input file")
    else:
        print("input file: " + sys.argv[1])                # if false make sure than evetything runs ok
        readCSVFile(sys.argv[1])


def readCSVFile(infile):

    with open(infile, 'rU') as csvfile:
        # using the dictionary reader
        reader = csv.DictReader(csvfile, delimiter=',')
        data = list(reader)
        print(data[160])


if __name__ == '__main__':
    main()
