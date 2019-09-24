# defining a function
def global_msj():
    print("We're done here... Bye")


# unpacking tuples
coordinates = (6, 2, 7)
x, y, z = coordinates

# dictionaries
customer = {
    "name": "Pedro Luis",
    "age": 33,
    "email": "pedro@gmail.com",
    "lenguage": "spanish",
    "is_verified": True
}
print(customer["name"])
print(customer.get("email", "no email"))

phone = input("Phone: " )
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven"
}
output = ""
for item in phone:
    output += digits_mapping.get(item, "!!") + " "
print(output)

# calling function global_msj
global_msj()

# defining a function
def user_name(first_name, last_name):
    print("Hi {} {}" .format(first_name, last_name))
    print("Welcome and Bye")

# calling function user_name
user_name("Monica", "Hadad")