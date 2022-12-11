# Initialise the starting position of the crates
ship = {
    '1':['T', 'P', 'Z', 'C', 'S', 'L', 'Q' , 'N'],
    '2':['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    '3':['D', 'C', 'Z', 'F'],
    '4':['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    '5':['P', 'W', 'C'],
    '6':['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    '7':['V', 'W', 'G', 'B', 'D'],
    '8':['N', 'J', 'S', 'Q', 'H', 'W'],
    '9':['R', 'C', 'Q', 'F', 'S', 'L', 'V']
 }

crates = ''
old = ''
new = ''
pointer = 0
i = 0

# Open the input file and seperate out the lines
with open("input.txt", "r") as file:
    for line in file:
        # Only run the code for moves
        if "m" in line:
            #itterate through each char in the line
            for char in line:
                if char == "v":
                    pointer = 0
                elif char.isnumeric() and pointer == 0:
                    crates += char
                elif char == "f":
                    pointer = 1
                elif char.isnumeric() and pointer == 1:
                    old += char
                elif char == "t":
                    pointer = 2
                elif char.isnumeric() and pointer == 2:
                    new += char
            # Cast string values to int
            crates = int(crates)
            # Move the crates
            for _ in range(crates):
                ship[new] += ship[old][-1]
                del ship[old][-1]
            # Reset the variable values after each full line loop
            crates, old, new = '', '', ''

final = ''

for key in ship:
    final += ship[key][-1]

print(final)