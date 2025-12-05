from random import randint

for i in range(0, 10):
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    ans = first_num + second_num
    xans = input("what is " + str(first_num) + " + " + str(second_num) + "?: \n")
    i = i + 1 
    if(str(xans) == str(ans)):
        print("correct")
    else:
        print("no, the answer is " + str(ans))
    