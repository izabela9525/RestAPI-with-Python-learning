# Reading data from the file
# object = open("D:\PY.txt", 'w')
## Update data in the file, delete old data and write new data
# object.write("Hello This is New Python File")
# object.close()

object = open("D:\PY.txt", 'a')
# Append new data in the file, it is mean thar we added new value to old value
object.write("Hello This is New Python File")
object.close()

