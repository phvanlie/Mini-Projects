# Open and Read a file
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)

# Write to a file
with open("file.txt", "w") as file:
    file.write("This is a sentence.")