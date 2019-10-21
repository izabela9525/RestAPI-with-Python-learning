# Reading data from the file

object = open("D:\PY.txt", 'r')

# # Read all characters from file and display 1 by 1
# for i in object.read():
#     print(i)

# Read all data from file line by line.
# If thera is some lines in the file print that values !!!
s = object.readline()
while(s):
    print(s)
    s = object.readline()