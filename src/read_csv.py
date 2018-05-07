import sys
import csv                      #we import the csv module


def main():
    if (len(sys.argv) != 2):                                #if there is more than one argument, then we need to say that
        print("this converter takes two parameters, "       #the converter takes one parameter as an input file
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        readCSVFile(sys.argv[1])                            #if false read csv file


def readCSVFile(infile):

    with open(infile, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')        #read the csv file in a much nicer format
        data = list(reader)
        print(data[161])


if __name__ == '__main__':
    main()
