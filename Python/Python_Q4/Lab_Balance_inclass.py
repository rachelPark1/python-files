def  balance(left, right):
    # returns 'Left', 'Right', or 'Balance'
    # depending on which side is heavier
    # left : string comprised of '!' and '?'
    # right : string compriesd of '!' and '?'


    #1) Find the total weight of the left side
    #a) declare and assign 0 to a running total
    leftTotal = 0
    #b) loop the same number of times as there are
    # items in left
    for char in left:
        #c) add the weight of the item to the
        # running total
        # (each item is represented by the variable
        # char)
        #i) is char an '!'?
        if char == "!":
            #if yes, add 3 to running total (leftTotal)
            leftTotal = leftTotal + 2
        #ii) otherwise, is char a '?'?
        elif char == "?":
            #if yes, add 3 to running total (leftTotal)
            leftTotal = leftTotal + 3
    #This print is for testing if Part 1 is correct
    print(leftTotal)
    #2) Find the total weight of the right side
    rightTotal = 0
    for char in right:
        if char == "!":
            rightTotal = rightTotal + 2
        elif char == "?":
            rightTotal = rightTotal + 3
    print(rightTotal)

    #3) Compare the total weight of the left side to
    # that of the right side
    # leftTotal : the total weight of left side
    # rightTotal : the total weight of right side
    #a) is leftTotal bigger than rightTotal?
        #return 'Left'
    #b) othewise, is rightTotal bigger than leftTotal?
        #return 'Right'
    #c) otherwise, is leftTotal and rightTotal equal?
        #return 'Balance'
    
    if leftTotal > rightTotal:
        return "Left"
    elif leftTotal < rightTotal:
        return "Right"
    elif leftTotal == rightTotal:
        return "Balance"

a = balance("!??!?!!!??", "?!!!!?!!?!")
print(a)
##a = "Hello World"
##for char in a:     # len(a) is not an iterable. It is an integer.
##    print(char)



##a = "Hello World"
##for char in a:     # len(a) is not an iterable. It is an integer.
##    print(char)
##    # It prints out
##    # H
##    # e
##    # l
##    # l
##    # o
##    #
##    # W
##    # o
##    # r
##    # l
##    # d
    
