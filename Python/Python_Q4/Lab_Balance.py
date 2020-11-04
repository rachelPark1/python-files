def balance(str1, str2):
    w1 = 0
    w2 = 0
    for char_index in range(len(str1)):
        if str1[char_index] == "!":
            w1 = w1 + 2
        elif str1[char_index] == "?":
            w1 = w1 + 3
    for char_index in range(len(str2)):
        if str2[char_index] == "!":
            w2 = w2 + 2
        elif str2[char_index] == "?":
            w2 = w2 + 3
##    print(w1)
##    print(w2)
    if w1 > w2:
        return "Left"
    elif w1 < w2:
        return "Right"
    elif w1 == w2:
        return "Balance"
    
a = balance("!!???!????", "??!!?!!!!!!!")
print(a)
