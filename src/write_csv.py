import sys
import csv
# import regular expressions modul
import re


# If the number of arguments does not equal 2 (true)
# then we need to say that the converter takes two parameters
def main():
    if (len(sys.argv) != 3):
        print("this converter takes two parameters, "
              "an input file and an output file")
    # if false read the csv dictionary file
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        readCSVDictFile(sys.argv[1], sys.argv[2])


# reading the dictionary file
def readCSVDictFile(infile, outfile):
    # accumulator - accumulates text
    fieldnames = []
    with open(infile, 'rU') as csvfile1:
        fieldreader = csv.reader(csvfile1, delimiter=',')
        # creating a list
        fielddata = list(fieldreader)[0]
        fieldnames = [make_nice_name(field) for field in fielddata]
    # open file
    with open(infile, 'rU') as csvfile2:
        # reading the data
        reader = csv.DictReader(csvfile2, delimiter=',')
        # putting the data into the list
        data = list(reader)

        with open(outfile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for d in data:
                newRow = {}
                for key, val in d.items():
                    # overwriting the keys in the dictionary
                    newRow[make_nice_name(key)] = d[key]

                writer.writerow(newRow)


def make_nice_name(name):
    # strip and replace space and underscore symbols
    newString = name.replace(" ", "_")
    newString = newString.replace("/", "_")
    newString = newString.strip("?").strip().lower()
    newString = re.sub(r'[^0-9a-z_\_]', '', newString)
    return newString


if __name__ == '__main__':
    main()
