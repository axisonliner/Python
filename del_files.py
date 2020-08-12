# Script for deleting files from a folder using the command line:
# command line: python del_files.py arg1 arg2
# - arg1 = folder path
# - arg2 = file extention
# Example: python del_files.py C:\Users\y.kondrashov\Desktop\ep0001 .exr

import os
import sys


def del_files(path, file):
    try:
        directory = str(sys.argv[1])
        for root, dirs, files in os.walk(directory):
            path = root.split(os.sep)
            for file in files:
                if file.endswith(str(sys.argv[2])):
                    path_to_file = '/'.join(path) + '/' + file
                    print("delete file: {}".format(path_to_file))
                    os.remove(path_to_file)
    
    except IndexError:
        print("Please, please provide two arguments:")
        print("arg1 = folder path")
        print("arg2 = file extention")
        print("Example: python del_files.py C:/Desktop/folder_name .exr")

if __name__ == '__main__':
    path = ""
    file = ""
    print
    del_files(path, file)
