import sys


def main():
    """interprets command line request
    Args:
        argv: an array with input and output files
    Returns:
        no return. Executed convertFile with collected
        file names.
    """

    # If the number of arguments does not equal 2 (true)
    # then we need to say that the converter takes two parameters
    if len(sys.argv) != 3:
        print("this converter takes two parameters, "
              "an input file and an output file")
    # if false convert the file
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        convertFile(sys.argv[1], sys.argv[2])

def convertFile(infile, outfile):
    """reads an infile which is decoded and then
        encoded into UTF8.
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Returns:
        doesn't return but writes the UTF encoded
        data to an outfile.
    """
    # we are opening the file
    f = open(infile, "rb")
    # reading the file
    data = f.read()
    # decoding
    decodedData = data.decode('ISO-8859-1')
    encodedData = decodedData.encode('utf-8')
    open(outfile, "wb").write(encodedData)
    # closing the file
    f.close()
    print("Success: File conversion complete.")


if __name__ == '__main__':
    main()
