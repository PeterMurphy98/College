def code_count(text):
    """Counts the number of times 'co{any-letter}e' appears in text."""
    # Initialise the code count to 0.
    code_count = 0
    # Loop through each letter
    for i in range(len(text)):
        # If the i-th letter is 'c', check if the next 3 leters are 'o', any letter, 'e'
        if text[i] == 'c':
            if text[i+1] == 'o' and text[i+2].isalpha() and text[i+3] == 'e':
                # If they are, add 1 to the code count
                code_count += 1
    return code_count

n = input("Enter text: ")
print(code_count(n))