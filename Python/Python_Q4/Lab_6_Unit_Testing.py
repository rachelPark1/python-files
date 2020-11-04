import unittest

### INPUT YOUR CODE BELOW, then run this file (F5)
### The function names must be count_duplicates, expanded_form_whole (for Part 1), and expanded_form (for Part 2) for this unit tester to work
def expanded_form_whole(wholeNum):
    # This function takes in an integer number bigger than 0
    # Make an empty list so that I can append expanded form of number
    ans = []
    listNum = list(str(wholeNum))
    # Loop as the same number as the number of characters in the wholeNum
    for i in range(len(listNum)):
        # i is 0, 1, 2
        #print(str(i) + "th item is " + listNum[i])
#        ten = 10 ** (len(listNum) - i - 1)
        #print("ten: " + str(ten))
#        c = int(listNum[i]) * ten
        # Unless listNum[i] is 0, append expanded form number to ans
        if int(listNum[i]) != 0:
            ans.append(str(listNum[i]) + "0" * (len(listNum) - i - 1))
        #print("ans: " + str(ans) + "\n")
    finalAns = " + ".join(ans)
    return finalAns

def expanded_form_whole_list(wholeNum):
    # This function takes in an integer number bigger than 0
    # Make an empty list so that I can append expanded form of number
    ans = []
    listNum = list(str(wholeNum))
    #print("listNum: " + str(listNum))
    # Loop as the same number as the number of characters in the wholeNum
    for i in range(len(listNum)):
        # i is 0, 1, 2, 3
        # Unless listNum[i] is 0, append expanded form number to ans
        #listNum[i]: 7, 0, 9, 0
        #print("listNum[i]: " + str(listNum[i]))
        if int(listNum[i]) != 0:
            ans.append(str(listNum[i]) + "0" * (len(listNum) - i - 1))
        #print("ans: " + str(ans) + "\n")
    return ans

def expanded_form(dec):
    # This function takes in decimal
    # Make an empty list so that I can append expanded form of number
    ans = []
    listDec= list(str(dec))
    #print("listDec: " + str(listDec))
    # Make a loop that finds where is a decimal point
    for i in range(len(listDec)):
        # i is 0, 1, 2, 3
        if listDec[i] == ".":
            listNum = listDec[0 : i]
            #print("listNum: " + str(listNum))
            listDec = listDec[(i + 1) : (len(listDec) + 1)]
            wholeNum = "".join(listNum)
            #print("wholeNum: " + str(wholeNum) + "\n")
            break
    # Make a loop that append expanded form of number
    for i in range(len(listDec)):
        # i is 0, 1
        #print("listDec: " + str(listDec))
        if int(listDec[i]) != 0:
            ans.append(str(listDec[i]) + "/1" + "0" * (i + 1))
        #print("ans: " + str(ans) + "\n")
    #print(str(expanded_form_whole_list(wholeNum)) + "\n")
    ans = expanded_form_whole_list(wholeNum) + ans
    ans = " + ".join(ans)
    return ans
    
    

m = expanded_form_whole(703040)
print(m)

##k = expanded_form(0.03040)
##print(k)


### INPUT YOUR CODE ABOVE, then run this file (F5)

class AllTests(unittest.TestCase):
    # This is the unit tester, if you want to test only one function, you can comment out its respective section


##    ### SECTION FOR DUPLICATES LAB START
##    known_values_dupes = (
##                    ("abcde", 0)
##                    ,("aabbcde", 2)
##                    ,("indivisibility", 1)
##                    ,("indivisibilities", 2)
##                    ,("aa11", 2)
##                    ,("abba", 2)
##                    )
##
##    def test_dupes(self):
##        for method_input, answer in self.known_values_dupes:
##            result = count_duplicates(method_input)
##            try:
##                self.assertEqual(answer, result)
##            except AssertionError:
##                print("For the input count_duplicates('%s'), the answer should be:\n%s\nbut received:\n%s\ninstead" % (method_input, answer, result))
##    ### SECTION FOR DUPLICATES LAB END

    ### SECTION FOR EXPANDED FORM P1 LAB START
    known_values_exp_form_whole = (
                    (12, "10 + 2")
                    ,(42, "40 + 2")
                    ,(4020, "4000 + 20")
                    ,(70304, "70000 + 300 + 4")
                    )

    def test_exp_form_whole(self):
        for method_input, answer in self.known_values_exp_form_whole:
            result = expanded_form_whole(method_input)
            try:
                self.assertEqual(answer, result)
            except AssertionError:
                print("For the input expanded_form_whole(%s), the answer should be:\n%s\nbut received:\n%s\ninstead" % (method_input, answer, result))
    ### SECTION FOR EXPANDED FORM P1 LAB END
##
##    ### SECTION FOR EXPANDED FORM P2 LAB START
##    known_values_exp_form = (
##                    (1.24, "1 + 2/10 + 4/100")
##                    ,(7.304, "7 + 3/10 + 4/1000")
##                    ,(0.04, "4/100")
##                    ,(0.007503, "7/1000 + 5/10000 + 3/1000000")
##                    ,(2070.057019, "2000 + 70 + 5/100 + 7/1000 + 1/100000 + 9/1000000")
##                    )
##
##    def test_exp_form(self):
##        for method_input, answer in self.known_values_exp_form:
##            result = expanded_form(method_input)
##            try:
##                self.assertEqual(answer, result)
##            except AssertionError:
##                print("For the input expanded_form(%s), the answer should be:\n%s\nbut received:\n%s\ninstead" % (method_input, answer, result))
##    ### SECTION FOR EXPANDED FORM P2 LAB END

if __name__ == "__main__":
    unittest.main()
