#  write a python program to print the contest of directory using the os module search online for the funnction which does that

import os

# Specify the directory path
path = '/'   # Replace with your directory path

# Print the contents of the directory
for item in os.listdir(path):
      print(item)


