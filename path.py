from pathlib import Path

# check existing directory
# path = Path("ecommerce")
# print(path.exists())

# create new directory
# path = Path("emails")
# path.mkdir()

# remove directory
# path = Path("emails")
# path.rmdir()

# global path
path = Path()
# all files .py on directory
for file in path.glob("*.py"):
    print(file)

# all files on directory
for file in path.glob("*"):
    print(file)