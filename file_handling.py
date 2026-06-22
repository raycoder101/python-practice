import sys
import os

f = open("demofile.txt", "r+")

#can't insert something at the beggining of a file
#but you can overwrite it
f.seek(0,0)
f.write("Add Stuff2!")

f.seek(0)
print(f.read())

f.seek(2)
f.write("Append Stuff!")

f.seek(0)
print(f.read())

f.close()
