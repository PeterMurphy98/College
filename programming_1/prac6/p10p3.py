st = input("Enter a string: ")
while (st != ""):
    count_v = 0
    i = 0
    while (i < len(st)):
        if (st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u'):
            count_v += 1
        i += 1

    print("Number of vowels equals ", count_v)
    st = input("Enter a string: ")
