# Ask the user to enter a string
text = input("Enter a string: ")
# Initialise the dog and cat counts to 0.
dog_count = cat_count = 0
# Loop through each letter
for i in range(len(text)):
    # If the i-th letter is 'd', check if the next 2 leters are 'og'
    if text[i] == 'd':
        # If they are, add 1 to the dog count
        if text[i+1] == 'o' and text[i+2] == 'g':
            dog_count += 1
    # If the i-th letter is 'c', check if the next 2 leters are 'at'
    if text[i] == 'c':
        # If they are, add 1 to the cat count
        if text[i+1] == 'a' and text[i+2] == 't':
            cat_count += 1

print("dog count =", dog_count)
print("cat count =", cat_count)