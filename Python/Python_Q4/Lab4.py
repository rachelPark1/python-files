def likes(List):
    # At first, this function takes in input list.
    # If the length of List is equal to 0 then return 'No one likes this.'
    if len(List) == 0:
        statement = "No one likes this."
        return statement
    elif len(List) == 1:
        statement = List[0] + " likes this."
        return statement
    # Otherwise, if a length of List is 2, then return the first
    #item of List and the second item of nameList likes this.
    elif len(List) == 2:
        statement = List[0] + " and " + List[1] + " like this."
        return statement
    # Otherwise, if a length of nameList is greater or equal to 3,
    elif len(List) >= 3:
        # If a length of List is greater than 3, then return
        #the first item of List, the second item of List, and
        #(len(List) - 2) others like this.
        if len(List) > 3:
            statement = List[0] + ", " + List[1] + ", and "+ str((len(List) - 2)) + " others like this."
            return statement
        # Otherwise, if a length of nameList is 3, then return the first
        #item of nameList, the second item of nameList, and the third
        #item of nameList likes this.
        elif len(List) == 3:
            statement = List[0] + ", " + List[1]  + ", and " + List[2] + " like this."
            return statement

a = likes(["a", "b", "c"])
print(a)
