##def repeatHelloWorld():
##    i = 0
##    while True:
##        print("Hello World")
##        if i > 3:
##            break
##        i = i + 1
##    print("End of program") ## Until now, we are just defining function.


fruits = ["Apple", "Banana", "Coconut", "Durian"]

def gramFruits():
    s = ""
    i = 0
    while i < len(fruits):
        if i == 0: #refers to 0th item of fruits
            s = s + fruits[i]
        elif i == (len(fruits) - 1): #refers to last item of fruits
            s = s + ", and " + fruits[i]
        else: #refers to any tiem that's not 0th or last
            s = s + ", " + fruits[i]
        i = i + 1
    print(s)

def returnFruitsStr():
    ## Prints 'Hello World' 5 times, and then EOP
    s = ""
    i = 0
    while i < len(fruits):
        if i == 0: #refers to 0th item of fruits
            s = s + fruits[i]
        elif i == (len(fruits) - 1): #refers to last item of fruits
            s = s + ", and " + fruits[i]
        else: #refers to any tiem that's not 0th or last
            s = s + ", " + fruits[i]
        i = i + 1
    return s

print("gramFruits(): ")
x = gramFruits()
print("returnFruitsStr(): ")
y = returnFruitsStr()

print("x: " + str(x))
print("y: " + str(y))

##def repeatHelloWorld(n, phrase):    # n --> any number that i want to repeat
##    ## Prints 'Hello World' n times, and then EOP
##    i = 0
##    while True:
##        print(phrase)
##        if i > (n - 2):
##            break
##        i = i + 1
##    print("End of program")
##
###repeatHelloWorld(9, "Sana is cute - Rachel")
##
##def fib(n):
##    if n == 1:
##        return 1
##    f = [1, 2]
##    fIndex = 2
##    while fIndex < n:
##        newF = f[-1] + f[-2]
##        f.append(newF)
##        fIndex = fIndex + 1
##    return f[-1]
##
##num = fib(1)
##print(num)
