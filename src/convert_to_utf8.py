import sys

def main():
     """interprets command line request
    Args:
        argv: an array with input and output files
    Returns:
        no return. Executed convertFile with collected
        file names.
    """
    if len(sys.argv) != 3:                                  #If the number of arguments does not equal 2 (true)
        print("this converter takes two parameters, "       #then we need to say that the converter takes two parameters
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])                 #if false convert the file
        print("output file: " + sys.argv[2])
        convertFile(sys.argv[1], sys.argv[2])

def convertFile(infile, outfile):       #defining a function called convertFile. It has two parameters.
    """reads an infile which is decoded and then
        encoded into UTF8.
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Returns:
        doesn't return but writes the UTF encoded
        data to an outfile.
    """                                    #infile is the file we are creating and outfile is the file that will be created
    f = open(infile, "rb")                                     #we are opening the file
    data = f.read()                                            #reading the file
    decodedData = data.decode('ISO-8859-1')                    #decoding
    encodedData = decodedData.encode('utf-8')
    open(outfile, "wb").write(encodedData)
    f.close()                                                  #closing the file
    print("Success: File conversion complete.")


if __name__ == '__main__':
    main()
