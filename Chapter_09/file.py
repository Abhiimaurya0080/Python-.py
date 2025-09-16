'''
two types of files 
1. text file(.txt, .c , etc)
Binary files (.jpg , .dat , etc )'''
#  <<<<<<<........................Here is a simple code to read a text file in python-------------------->>>>>>>
# data = Abhii is a  good boy 
f = open("file.txt ")
data = f.read()
print (data)
f.close()