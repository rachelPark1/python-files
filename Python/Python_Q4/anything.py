def count_duplicates(strAlpha):
    listAlpha = list(strAlpha)
    dupChar = []
    for i in range(len(listAlpha)):
        newAlpha = listAlpha[0 : i] + listAlpha[(i + 1) : len(listAlpha)]
        if listAlpha[i] in newAlpha:
            if not (listAlpha[i] in dupChar):
                dupChar.append(listAlpha[i])
                newAlpha.remove(listAlpha[i])
    return len(dupChar)
    

p = count_duplicates("aabb")
print(str(p) + "\n")

# -----------------------------------------------------

def expanded_form_whole(wholeNum):
    ans = []
    listNum = list(str(wholeNum))
    for i in range(len(listNum)):
        if int(listNum[i]) != 0:
            ans.append(str(listNum[i]) + "0" * (len(listNum) - i - 1))
    return " + ".join(ans)

    
p = expanded_form_whole(703040)
print(str(p) + "\n")

# -----------------------------------------------------

def expanded_form(dec):
    ans = []
    listDec = list(str(dec))
    for char in range(len(listDec)):
        if listDec[char] == ".":
            listNum = listDec[0 : char]
            listDec = listDec[(char + 1) : len(listDec)]
            semiAns = expanded_form_num(listNum)
            break
    for i in range(len(listDec)):
        if int(listDec[i]) != 0:
            ans.append(str(listDec[i])  + "/1" + "0" * (i + 1))
    ans = semiAns + ans
    return " + ".join(ans)

def expanded_form_num(num):
    ans1 = []
    for i in range(len(num)):
        if num[i] != "0":
            ans1.append(num[i] + "0" * (len(num) - i - 1))
    return ans1
            
    
p = expanded_form(102.08920)
print(str(p) + "\n")

# -----------------------------------------------------

def diamond(n):
    upper = ""
    lower = ""
    if n % 2 != 0:# if n is odd number,
        i = 1
        print(((n // 2) + 1))
        while i <= ((n // 2) + 1):
            upper = upper + " " * (n - i -1) + "*" * (2 * i - 1) + "\n"
            i = i + 1
        i = ((n // 2) + 1)
        while i > 0:
            lower = lower + " " * (n - i) + "*" * (2 * i - 3) + "\n"
            i = i - 1
    elif n % 2 == 0:
        print(n // 2)
        i = 1
        while i <= (n // 2):
            upper = upper + " " * (n - i - 1) + "*" * (2 * i - 1) + "\n"
            i = i + 1
        i = ((n // 2) + 1)
        while i > 0:
            lower = lower + " " * (n - i) + "*" * (2 * i - 3) + "\n"
            i = i - 1
    dia = upper + lower
    return dia
    
p = diamond(7)
print(p)
