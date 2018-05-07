import sys
import csv
import re                                              #import regular expressions modul

def main():
    if (len(sys.argv) != 3):                                #If the number of arguments does not equal 2 (true)
        print("this converter takes two parameters, "       #then we need to say that the converter takes two parameters
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])                 #if false read the csv dictionary file
        print("output file: " + sys.argv[2])
        readCSVDictFile(sys.argv[1], sys.argv[2])

def readCSVDictFile(infile, outfile):                   #reading the dictionary file.

    fieldnames = []                                     #accumulator - accumulates text
    with open(infile, 'rU') as csvfile1:
        fieldreader = csv.reader(csvfile1, delimiter=',')
        fielddata = list(fieldreader)[0]                #creating a list
        fieldnames = [make_nice_name(field) for field in fielddata]

    with open(infile, 'rU') as csvfile2:  # open file
        reader = csv.DictReader(csvfile2, delimiter=',') #reading the data
        data = list(reader)                              # putting the data into the list

        with open(outfile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for d in data:
                newRow = {}
                for key, val in d.items():
                    newRow[make_nice_name(key)] = d[key]       #overwriting the keys in the dictionary

                writer.writerow(newRow)


def make_nice_name(name):

    newString = name.replace(" ", "_")                  #strip and replace space and underscore symbols
    newString = newString.replace("/", "_")
    newString = newString.strip("?").strip().lower()
    newString = re.sub(r'[^0-9a-z_\_]', '', newString)
    return newString


if __name__ == '__main__':
    main()

