num = 0

if num > 10:
    num = str(num)
    print(num + " is bigger than 10")
    print("What a big number!")
elif num == 10:
    num = str(num)
    print(num + " equals 10")
    print("I love the number 10")
else:
    if num == 5:
        print("I love 5")
    elif num == 7:
        print("Lucky 7")
    elif num == 3:
        print("3 strikes and you're out")
    num = str(num)
    print(num + " is 10 or smaller")
    print("What a small number")    ##TYPE 2 : if we comment this part, then it results in just "End of Program."
print("End of Program")
