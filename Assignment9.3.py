# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
import os
import sys

def CheckFileExists(file_name):
    for folder,subfolder,file in os.walk("./"):
        #print("The folder is:",folder)
        #print("The subfolder is:",subfolder)
        #print("The file is:",file)
        if file_name in file:
            print("Given file exist at:",file_name )
            fl_in = open(file_name, 'r')
            fl_out = open('demo.txt', 'w')
            for line in fl_in:
                fl_out.write(line)
            fl_in.close()
            fl_out.close()
        else:
            print("The given file does not exists")
def main():
    CheckFileExists(sys.argv[1])

if __name__ == "__main__":
    main()
