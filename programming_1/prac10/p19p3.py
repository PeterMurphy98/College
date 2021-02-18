def counts(page):
    """Counts all brackets in page and prints if they are balanced or not."""
    # Read the page into the string s
    s = page.read()
    # Count different brackets
    print(f"( count = {s.count('(')}")
    print(f") count = {s.count(')')}")
    print(f"[ count = {s.count('[')}")
    print(f"] count = {s.count(']')}")
    print("{", f"count = {s.count('{')}")
    print("}", f"count = {s.count('}')}")
    print(f"< count = {s.count('<')}")
    print(f"> count = {s.count('>')}")
    # Print if brackets are balanced or not.
    if s.count('(') == s.count(')'):
        print("( and ) are balanced.")
    else:
        print("( and ) are not balanced.")
    if s.count('[') == s.count(']'):
        print("[ and ] are balanced.")
    else:
        print("[ and ] are not balanced.")
    if s.count('{') == s.count('}'):
        print("{ and } are balanced.")
    else:
        print("{ and } are not balanced.")
    if s.count('<') == s.count('>'):
        print("< and > are balanced.")
    else:
        print("< and > are not balanced.")

counts(open("index.html", "r"))