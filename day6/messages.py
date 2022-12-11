# Open the input file and seperate out the lines
with open("input.txt", "r") as f:
    signal = f.read()

# Initialise a counter
i = 0
# Looking for a string of fixed length, 14
length = 14

# Loop over each char in signal
for char in signal:
    # If the set(14 items) == 14 (length) then we have a winner
    if len(set(signal[i:i+length])) == length:
        # Print the list number of the last item in the unique string
        print(i+length)
        break
    else:
        i+=1