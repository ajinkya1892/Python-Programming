# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous
# Search "Marvellous" in Demo.txt


import os
import sys
import re
def CheckFileExists(file_1,string_name):
    counter = 0
    for folder,subfolder,file in os.walk("./"):
        if file_1 in file:
            print("Given file exist at:",file_1 )
            fl_1 = open(file_1, 'r')
            for line in fl_1:
                print line
                if re.search(string_name,line):
                    counter+=1
            fl_1.close()
            print(counter)
            print("Given string appears %d times file"%(counter))

        else:
            print("The given file does not exists")
def main():
    CheckFileExists(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
