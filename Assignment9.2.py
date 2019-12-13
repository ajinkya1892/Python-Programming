# 2. Write a program which accept file name from user and open that file and display the contents
# of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os
import sys

def CheckFileExists(file_name):
    for folder,subfolder,file in os.walk("./"):
        #print("The folder is:",folder)
        #print("The subfolder is:",subfolder)
        #print("The file is:",file)
        if file_name in file:
            print("Given file exist at:",file_name )
            fl = open(file_name, 'r')
            print(fl.read())
            fl.close()
        else:
            print("The given file does not exists")
def main():
    CheckFileExists(sys.argv[1])

if __name__ == "__main__":
    main()
