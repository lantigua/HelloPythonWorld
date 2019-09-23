number_list1 = [2, 2, 8, 9, 9, 2, 3, 2, 8, 10, 10]
total = 0
for item in number_list1:
    total += item
    cuc_total = total * 25
print("Total: ${}".format(total))
str = "Total CUC: ${}"
print(str.format(cuc_total))

#--------------------------------------------------

for x_s in number_list1:
    output = ""
    for count in range(x_s):
        output += "*"
    print(output)