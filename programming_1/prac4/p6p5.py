pword = 'password'

attempt = input('Password: ')
if (attempt == pword):
    print('You have successfully logged in.')
    exit()

else:
    print('Sorry, the password is wrong. Please enter the correct password 3 times.')
    att1 = input('Password: ')
    att2 = input('Password: ')
    att3 = input('Password: ')
    if (att1 == att2 == att3 == pword):
        print('You have successfully logged in.')
        exit()
    else:
        print('You have been denied access.')
        exit()



