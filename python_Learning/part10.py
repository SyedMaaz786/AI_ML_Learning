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

