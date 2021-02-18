def counts(page):
    """Returns different string counts to results.txt."""
    # Read the page into the string s
    s = page.read()
    # Create results file
    results = open("results.txt", "w")
    # Count number of newlines in s
    newline_c = s.count('\n')
    # Count different strings and write to results
    results.write(f"< count = {s.count('<')}\n")
    results.write(f"> count = {s.count('>')}\n")
    results.write(f"\\n = {newline_c}\n")
    results.write(f"e count = {s.count('e')}\n")
    results.write(f"<!-- count = {s.count('<!--')}\n")
    results.write(f"--> count ={s.count('-->')}\n")

counts(open("index.html", "r"))