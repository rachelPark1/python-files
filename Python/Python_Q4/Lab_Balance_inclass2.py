def weightObjects(items):
    # takes in a bunch of objects
    # and returns the total weight of the objects
    # items : string comprised of '!' and '?'
    itemsTotal = 0
    for char in items:
        if char == "!":
            itemsTotal = itemsTotal + 2
        elif char == "?":
            itemsTotal = itemsTotal + 3
    return itemsTotal

##w = weightObjects('??!')
##print("w: " + str(w))

def  balance(left, right):
    # returns 'Left', 'Right', or 'Balance'
    # depending on which side is heavier
    # left : string comprised of '!' and '?'
    # right : string compriesd of '!' and '?'


    #1) Find the total weight of the left side
    #a) declare and assign 0 to a running total

    leftTotal = weightObjects(left) # Part 1
    rightTotal = weightObjects(right) # Part 2

    
    if leftTotal > rightTotal:
        return "Left"
    elif leftTotal < rightTotal:
        return "Right"
    elif leftTotal == rightTotal:
        return "Balance"

a = balance("!!!!", "??")
print(a)
