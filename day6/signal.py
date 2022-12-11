
# Open the input file and seperate out the lines
with open("input.txt", "r") as f:
    signal = f.read()

#initialise counter
i = 0

# Loop through each char in signal
for char in signal:
    # compare each char to the other 3 in the string
    if signal[i] == signal[i+1]: 
        i+=1
    elif signal[i+1] == signal[i+2]: 
        i+=1
    elif signal[i+2] == signal[i+3]: 
        i+=1
    elif signal[i] == signal[i+2]: 
        i+=1
    elif signal[i+1] == signal[i+3]: 
        i+=1
    elif signal[i] == signal[i+3]:
        i+=1
    else:
        print(i+4)
        break
    

