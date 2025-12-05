
first = input("first number: ")
second = input("second number: ")
if (second == 0):
    print("cant divide by '0'")
    breakpoint
ans1 = int(first) + int(second)
ans2 = int(first) - int(second)
ans3 = int(first) * int(second)
ans4 = int(first) / int(second)
print(str(ans1) + str(' (+)'))
print(str(ans2) + str(' (-)'))
print(str(ans3) + str(' (x)'))
print(str(ans4) + str(' (÷)'))