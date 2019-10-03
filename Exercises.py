import utils

number_list1 = [2, 2, 8, 9, 9, 2, 3, 2, 8, 10, 10]
total = 0
for item in number_list1:
    total += item
    cuc_total = total * 25
print("Total: ${}".format(total))
str = "Total CUC: ${}"
print(str.format(cuc_total))

# --------------------------------------------------

uniques_numbers = []
for numbers in number_list1:
    if numbers not in uniques_numbers:
        uniques_numbers.append(numbers)
print(uniques_numbers)
uniques_numbers.sort()
print(uniques_numbers)

# --------------------------------------------------

for x_s in number_list1:
    output = ""
    for count in range(x_s):
        output += "*"
    print(output)

# ---------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for filas in matrix:
    for cosas in filas:
        print("cosas de las filas {}".format(cosas))
# ---------------------------------------------------


list1 = [23, 25, 45, 72, 12, 66, 45, 65]
maximum = utils.find_max(list1)
print("The largest number in the list is {}".format(maximum))



