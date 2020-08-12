# Script for deleting files from a folder using the command line:
# command line: python del_files.py arg1 arg2
# - arg1 = folder path
# - arg2 = file extention
# Example: python del_files.py C:\Desktop\folder_name .exr

import os
import sys
import math

def get_size(filename):
    st = os.stat(filename)
    return st.st_size


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "{0} {1}".format(s, size_name[i])


def del_files(path, file):
    files_size = 0
    file_num = 0
    try:
        directory = str(sys.argv[1])
        ext_file = str(sys.argv[2])
        for root, dirs, files in os.walk(directory):
            path = root.split(os.sep)
            for file in files:
                if file.endswith(ext_file):
                    path_to_file = '/'.join(path) + '/' + file
                    files_size += get_size(path_to_file)
                    print("delete file: {}".format(path_to_file))
                    os.remove(path_to_file)
                    file_num += 1
        if not file_num:
            print("'{}' files not found".format(ext_file))
        else:
            print
            print("{} - files have been deleted".format(file_num))
            print("{} - total file size".format(convert_size(files_size)))
                
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
