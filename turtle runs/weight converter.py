weight = input("weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converdted = float(weight) // float(0.45)
    print("weight in pounds(lbs) is " + str(converdted))
else:
    converdted = float(weight) * float(0.45)
    print("weight in kilograms(kg) is " + str(converdted))
