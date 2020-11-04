def add(computer, no2): # give two data
    result = computer + no2
    return result

##x = add(5, 6)
##print(x)

def asmr(no1, no2):
    a = no1 + no2
    s = no1 - no2
    m = no1 * no2
    r = no1 % no2
    print("What operator do you want to use? (asmr)")
    ch = input()
    if ch == "a":
        return a
    elif ch == "s":
        return s
    elif ch == "m":
        return m
    elif ch == "r":
        return r

##x = asmr(10, 4)
##print("x : " + str(x))

def printValueData(data):
    dataType = type(data)
    s = ""
    s = s + "value: " + str(data)
    s = s + ", data type: " + str(dataType)
    return s

x = round(54254235.00)
print(printValueData(x))
