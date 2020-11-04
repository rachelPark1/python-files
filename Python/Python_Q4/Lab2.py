
def sortString(random):
    listString = random.split(" ")
 #   print(listString)
    final = ['', '', '', '', '', '', '', '', '']
    for item in range(len(listString)):
        # item is 0, 1, 2, 3, 4, 5
##        for char in item:
##        # char is the each item in item.
##        # char is 'N', '3', 'c', etc.
##        print("item: " + str(listString[item]))
        
        if "1" in listString[item]:
            final[0] = listString[item]
        elif "2" in listString[item]:
            final[1] = listString[item]
        elif "3" in listString[item]:
            final[2] = listString[item]
        elif "4" in listString[item]:
            final[3] = listString[item]
        elif "5" in listString[item]:
            final[4] = listString[item]
        elif "6" in listString[item]:
            final[5] = listString[item]
        elif "7" in listString[item]:
            final[6] = listString[item]
        elif "8" in listString[item]:
            final[7] = listString[item]
        elif "9" in listString[item]:
            final[8] = listString[item]
#        print("final: " +str(final))
        finalStr = " ".join(final)
    
    return finalStr
            

a = sortString("N3ice Worl2d me5et yo6u Hell1o t4o")
print(a)

# Result : Hell1o Worl2d N3ice t4o me5et yo6u


##hello = "Hello World"
##print(hello)
##helloList = list(hello)
##print(helloList)
##helloJoin = "!".join(helloList)
##print(helloJoin)




# random : string with Arabic number included
# random : str

# split string in random into each word in a list

# Make a function that:
#1) find the word that has 1
    # Step 1) remove that word from the original list
    # Step 2) append that word to the final list that you are going to return
    # Make another function that do Step 1 and Step 2
    
#2) find the word that has 2
    # Step 1) remove that word from the original list
    # Step 2) append that word to the final list that you are going to return
    # Make another function that do Step 1 and Step 2
    
#3) find the word that has 3
    # Step 1) remove that word from the original list
    # Step 2) append that word to the final list that you are going to return
    # Make another function that do Step 1 and Step 2
    
#4) find the word that has 4
    #set the word as item 4
#5) find the word that has 5
    #set the word as item 5
#6) find the word that has 6
    #set the word as item 6
#7) find the word that has 7
    #set the word as item 7
#8) find the word that has 8
    #set the word as item 8
#9) find the word that has 9
    #set the word as item 9
