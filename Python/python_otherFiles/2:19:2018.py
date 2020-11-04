##num = 5.0 // "2"
##print(num) ## Error

print("Hello World. This is the start of the program.
word = input()

print("You typed: " + word)
print("End of Program")

print("Type in a number: ")
num = input()
num2 = int(num) +9
print("Yout typed: " +num)
num2 = str(num2)
print(num + " + 9 = " + num2)  ## Here, num2 was an integer.
print("End of Program")

a = int(5.0)
print(a)
a = int(5.3)
print(a)
a = float(5)
print(a)
a = str(5.3)
print(a)
a = float("5.3") ## result in 5.3, float() changes the data type
print(a)
a = int("5.3") ## error
print(a)
a = float("5.3")
a = int(a)
print(a)
a = int(float("5.3"))
print(a)

print("5.7" + str(3))
print(float("5.7") + 3)

print("Hello World.\nStart the program")
one = input()
two = input()
print("You typed: " + one + two)
print("End the program")

print(all("hi"))

