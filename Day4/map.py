line1 = [" ", " ", " "] 
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the sport")
position = input("Input your coordinate using a - c and 1 - 3. Example; B3\n").lower()

i = ['a', 'b', 'c']
longitude = i.index(position[0])
latitude = int(position[1]) - 1
map[longitude][latitude] = "X"

print(f"{line1}\n{line2}\n{line3}")