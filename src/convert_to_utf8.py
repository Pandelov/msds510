import sys

def main():
    if len(sys.argv) != 3:
        print("this converter takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        convertFile(sys.argv[1], sys.argv[2])

def convertFile(infile, outfile):       #defining a function called convertFile. It has two parameters.
                                        #infile is the file we are creating and outfile is the file that will be created
    f = open(infile, "rb")                                     #we are opening the file
    data = f.read()                                            #reading the file
    decodedData = data.decode('ISO-8859-1')                    #decoding
    encodedData = decodedData.encode('utf-8')
    open(outfile, "wb").write(encodedData)
    f.close()                                                  #closing the file
    print("Success: File conversion complete.")


if __name__ == '__main__':
    main()
