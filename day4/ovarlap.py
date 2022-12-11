i = 0
tmp1 = ''
tmp2= ''
tictac = True
elves = dict.fromkeys(range(2000))

with open("input.txt", "r") as file:
    for line in file:
        for char in line:
            
            if char.isnumeric() and tictac == True:
                tmp1 += char
            
            elif char.isnumeric() and tictac == False:
                tmp2 += char
            
            elif char == '-':
                tictac = not tictac
            
            elif char == "," or char == "\n":
                elves[i] = [*range(int(tmp1), (int(tmp2)+1))]
                tmp1 = ''
                tmp2= ''
                i += 1
                tictac = not tictac

total = 0

for i in range(0, 2000, 2):
    if elves[i][0] in elves[i+1] or elves[i][-1] in elves[i+1]:
        total += 1
    elif elves[i+1][0] in elves[i] or elves[i+1][-1] in elves[i]:
        total += 1

print(total)
