# File Handling Modes

# w → write (creates or overwrites)
f = open("sample.txt", "w")
f.write("Writing using write mode.\n")
f.writelines = ["Writing using writelines mode.\n"
             "Second line using writelines mode.\n"]
f.close()

# r → read
f = open("sample.txt", "r")
print(f.read())        # reads the entire file
f.seek(0)
print(f.readline())    # reads the first line
f.seek(0)
print(f.readlines())   # reads all lines into a list
f.close()

# a → append
f = open("sample.txt", "a")
f.write("Appending using a mode.\n")
f.close()

# r+ → read + write (keeps old content)
f = open("sample.txt", "r+")
print(f.read())
f.write("Added using r+ mode.\n")
f.close()

# w+ → write + read (clears old content)
f = open("sample.txt", "w+")
f.write("New content from w+ mode.\n")
f.seek(0)
print(f.read())
f.close()

# a+ → append + read
f = open("sample.txt", "a+")
f.write("Adding using a+ mode.\n")
f.seek(0)
print(f.read())
f.close()

# x → create new file (fails if exists)
f = open("sample2.txt", "x")
f.write("Created using x mode.\n")
f.close()

# wb → write binary
f = open("binary.bin", "wb")
f.write(b"Binary data from wb mode")
f.close()

# rb → read binary
f = open("binary.bin", "rb")
print(f.read())
f.close()

# wb+ → write + read binary
f = open("binary2.bin", "wb+")
f.write(b"Binary data from wb+ mode")
f.seek(0)
print(f.read())
f.close()

# rb+ → read + write binary
f = open("binary2.bin", "rb+")
print(f.read())
f.write(b"\nMore binary data from rb+ mode")
f.close()

# WITH KEYWORD 

with open("sample.txt", "w") as f:
    f.write("This file was created using the with keyword.\n")

with open("sample.txt", "r") as f:
    print(f.read())

    # DELETE FILES

import os

os.remove("binary.bin")
os.remove("binary2.bin")
os.remove("with_example.txt")