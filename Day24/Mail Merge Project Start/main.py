# Open the file and store the letter as variables.
with open("./100-Day-of-coding-python/Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as startLetter:
    toEdit = startLetter.read()

# Open the file and store the letter as variables.
with open("./100-Day-of-coding-python/Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    toAdd = names.read()

# Make the names into a list
nameList = toAdd.split()

# Iterate through the list of names
for name in nameList:

    # Replace the [name] with a name in the list
    newLetter = toEdit.replace("[name]", name)

    # Write a new letter and save it
    with open(f"./100-Day-of-coding-python/Day24/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as editedLetter:
        editedLetter.write(newLetter)
