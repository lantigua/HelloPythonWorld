import math
import converters
from converters import lbs_to_kg

print("This's my weight in kg {} " .format(lbs_to_kg(210)))

print("This's my weight in lbs {} " .format(converters.kg_to_lbs(92)))

info = 'Python is an interpreted, high-level, general-purpose programming language.'
print(info)
print(info[-1])
print(info[0:6])
print(info[-9:-1])

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(age)
print(type(age))

lbs_weight = input("Weight (Lbs): ")
kg_weight = 0.45 * int(lbs_weight)
print(kg_weight)
print("things")
x = -2.9
print(abs(x))