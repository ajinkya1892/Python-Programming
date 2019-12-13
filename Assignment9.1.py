# 1.Write a program which accepts file name from user and check whether that file exists in
# current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

import os
import sys

def CheckFileExists(file_name):
    for folder,subfolder,file in os.walk("./"):
        #print("The folder is:",folder)
        #print("The subfolder is:",subfolder)
        #print("The file is:",file)
        if file_name in file:
            print("Given file exist at:",file)
        else:
            print("The given file does not exists")
def main():
    CheckFileExists(sys.argv[1])

if __name__ == "__main__":
    main()
