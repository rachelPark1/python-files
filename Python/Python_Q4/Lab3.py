def diamond(n):
    # n : positive integer
    # Takes in n
    #1) If n is an odd number, then make ((n // 2) + 1) space and put 1 *
        #a) Make 1 less space than the previous one and put 2 more *
        #b) Do Step a until line ((n // 2) + 1)
        #c) Make 1 more space than the previous one and put 2 less *
        #d) Do Step c until number of * gets smaller than 0
    # Return diamond(?)
    upper = ""
    lower = ""
    if n % 2 != 0: # When n is odd number,
        i = 1
        while i <= ((n // 2) + 1): # n // 2 + 1 is 3.
            upper = upper + " " * (n - i - 1) + "*" * (2 * i - 1) + "\n"
            #print(upper)
            i = i + 1
        i = ((n //2) + 1) # i is 3.
        while i > 0:
            lower = lower + " " * (n - i) + "*" * ( 2 * i - 3) + "\n"
            #print(lower)
            i = i - 1
    #2) Otherwise, if n is an even number, then make (n - 2) space and put 1 *
        #a) Make 1 less space than the previous one and put 2 more *
        #b) Do Step a until line (n // 2)
        #c) Make 1 more space than the previous one and put 2 less *
        #d) Do Step c until number of * gets smaller than 0
    # Return diamond(?)
    
    elif n % 2 == 0: # When n is even number,
        i = 1
        while i <= (n // 2): # n // 2 is 4.
            upper = upper + " " * (n - i - 1) + "*" * (2 * i - 1) + "\n"
            #print(upper)
            i = i + 1
        i = ((n //2) + 1) # i is 4
        while i > 0:
            lower = lower + " " * (n - i) + "*" * ( 2 * i - 3) + "\n"
            #print(lower)
            i = i - 1
    dia = upper + lower
    return dia
        
a = diamond(5)
print(a)
