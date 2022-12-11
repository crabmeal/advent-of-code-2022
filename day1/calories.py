calories1 = 0
calories2 = 0
calories3 = 0

tmp = 0

with open("input.txt", "r") as file:
    data = file.readlines()
  
for i in data:
    if i != '\n':
        tmp += int(i)
    elif tmp > calories1:
        calories2 = calories1
        calories1 = tmp
        tmp = 0
    elif tmp > calories2:
        calories3 = calories2
        calories2 = tmp
        tmp = 0
    elif tmp > calories3:
        calories3 = tmp
        tmp = 0
    else:
        tmp = 0

print(calories1 + calories2 + calories3)


