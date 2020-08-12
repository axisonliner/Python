import os
import sys

directory = str(sys.argv[1])
# directory = "C:/Users/y.kondrashov/Desktop/ep0001/"

for root, dirs, files in os.walk(directory):
    path = root.split(os.sep)
    for file in files:
    	if file.endswith(str(sys.argv[2])):
    		path_to_file = '/'.join(path) + '/' + file
    		print("delete file: {}".format(path_to_file))
    		os.remove(path_to_file)
        