
total = 0

with open("input.txt", "r") as file:
    data = file.readlines()
    
for i in data:
    i = i.strip()
    if i == "A X": 
        total += 3
    elif i == "A Y":
        total += 4
    elif i == "A Z":
        total += 8
    elif i == "B X":
        total += 1
    elif i == "B Y":
        total += 5
    elif i == "B Z":
        total += 9
    elif i == "C X":
        total += 2
    elif i == "C Y":
        total += 6
    elif i == "C Z":
        total += 7

print(total)


    