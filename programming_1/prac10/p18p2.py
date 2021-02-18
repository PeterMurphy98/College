def code_count(text):
    """Counts the number of times 'code' appears in text."""
    return text.count('code')

n = input("Enter text: ")
print(code_count(n))