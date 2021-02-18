pword = 'password'

attempt = input('Password: ')
if (attempt == pword):
    print('You have successfully logged in.')
    exit()

n = 1
while(attempt != pword):
    attempt = input ('Incorrect password, try again:')
    n += 1
    if (attempt == pword):
        print('You have successfully logged in.')
        exit()

    if (n == 3):
        print('You have been denied access.')
        exit()



