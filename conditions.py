# example I
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear warm clothe")
else:
    print("its a lovely day")
print("Enjoy your day")

# example II
good_credit = False
price = 1000000
if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print("Down Payment: ${}".format(down_payment))

# example III
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print("You're {} kilos".format(converted))
else:
    converted = weight / 0.45
    print("You're {} pounds".format(converted))

