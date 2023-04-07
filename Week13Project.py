#!/usr/bin/env python

import os

# Get the current working directory
cwd = os.getcwd()

# Initialize an empty list to store the file information
files = []

# Loop through each file in the directory
for filename in os.listdir(cwd):

    # Get the size of the file in bytes
    size = os.path.getsize(filename)

    # Add the file name and size to the list of files
    files.append({'name': filename, 'size': size})

# Print the list of files
print(*files,sep="\n")