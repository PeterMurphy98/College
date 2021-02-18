# start while loop
day_num = 1
while (day_num >= 0):
    # ask user for day number
    day_num = int(input("Enter the day for which you want to find the date (an integer): "))
    print("You entered: ", day_num)

    # if the number is less than or equal to 30 
    if (day_num >= 1 and day_num <= 30):
        # day of the month equals the day number
        day_month = day_num
        month = "September 2020"

    # else if the number is greater than 30 
    elif (day_num >= 31 and day_num <= 61):
        # day of the month equals the day number minus the total days in all the previous months
        day_month = day_num - 30
        month = "October 2020"

    elif (day_num >= 62 and day_num <= 91):
        day_month = day_num - (30+31)
        month = "November 2020"

    elif (day_num >= 92 and day_num <= 122):
        day_month = day_num - (30+31+30)
        month = "December 2020"

    elif (day_num >= 123 and day_num <= 153):
        day_month = day_num - (30+31+30+31)
        month = "January 2021"

    elif (day_num >= 154 and day_num <= 181):
        day_month = day_num - (30+31+30+31+31)
        month = "February 2021"

    elif (day_num >= 182 and day_num <= 212):
        day_month = day_num - (30+31+30+31+31+28)
        month = "March 2021"

    elif (day_num >= 213 and day_num <= 242):
        day_month = day_num - (30+31+30+31+31+28+31)
        month = "April 2021"

    elif (day_num >= 243 and day_num <= 273):
        day_month = day_num - (30+31+30+31+31+28+31+30)
        month = "May 2021"

    elif (day_num >= 274 and day_num <= 303):
        day_month = day_num - (30+31+30+31+31+28+31+30+31)
        month = "June 2021"

    elif (day_num >= 304 and day_num <= 334):
        day_month = day_num - (30+31+30+31+31+28+31+30+31+30)
        month = "July 2021"

    elif (day_num >= 335 and day_num <= 365):
        day_month = day_num - (30+31+30+31+31+28+31+30+31+30+31)
        month = "August 2021"

    # else if the number is 0
    elif (day_num == 0):
        print("Finished!")
        continue

    # else if the number is negative
    elif (day_num < 0):
        print("Error: Day number cannot be negative.")
        break

    # if the number isn't in the academic year
    else: 
        print("Day number", day_num, "is not in the 2020-2021 academic yer!")
        continue

    print("Day number", day_num, "is", day_month, month)