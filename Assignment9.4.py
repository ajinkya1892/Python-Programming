# 4.Write a program which accept two file names from user and compare contents of both the
# # files. If both the files contains same contents then display success otherwise display failure.
# # Accept names of both the files from command line.
# # Input : Demo.txt Hello.txt
# # Compare contents of Demo.txt and Hello.txt

import os
import sys

def CheckFileExists(file_1,file_2):
    for folder,subfolder,file in os.walk("./"):
        if file_1 in file and file_2 in file:
            print("Given file exist at:",file_1,file_2 )
            fl_1 = open(file_1, 'r')
            fl_2 = open(file_2, 'r')
            for line1,line2 in zip(fl_1,fl_2):
                if line1 == line2:
                    flag = 1
                else:
                    flag = 0
            fl_1.close()
            fl_2.close()

            if flag==0:
                print("Failure")
            else:
                print("Success")
        else:
            print("The given file does not exists")
def main():
    CheckFileExists(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
