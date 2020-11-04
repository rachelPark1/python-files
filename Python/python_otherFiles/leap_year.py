print("Do you want to know when is a leap year?")
print("Then, type in the year that you want to know!")

##year = input()
##if float(year) >= 0:
##    if float(year) < 100:
##        if float(year) % 4 == 0:
##            print("That year is a leap year!")
##        else:
##            print("That year isn't a leap year.")
##    if float(year) == 100:
##        print("That year isn't a leap year.")
##else:
##    print("That's not possible. Sorry..")
##if float(year) > 100:
##    if float(year) % 4 == 0:
##        if float(year) % 100 != 0:
##            print("That year is a leap year!")
##        elif float(year) % 400 == 0:
##            print("That year is a leap year!")
##    else:
##        print("That year isn't a leap year.")
##print("End of Program")

year = input()
if float(year) >= 0:
    if float(year) % 4 == 0:
        if float(year) % 400 == 0:
            print("That year is a leap year!")
        elif float(year) % 100 == 0:
            print("That year isn't a leap year.")
        else:
            print("That year is a leap year!")
    else:
        print("That year isn't a leap year.")
else:
    print("That's not possible! Sorry..")

print("End of Program")
