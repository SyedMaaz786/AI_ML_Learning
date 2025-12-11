# File Modes in Python

# w → write (creates or overwrites)
f = open("sample.txt", "w")
f.write("Writing using w mode.\n")
f.close()

# r → read
f = open("sample.txt", "r")
print(f.read())
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