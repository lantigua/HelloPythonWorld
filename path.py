from pathlib import Path

# check existing directory
path = Path("ecommerce")
print(path.exists())

# create new directory
path = Path("emails")
path.mkdir()

# global path
glob_path = Path()
print(glob_path.glob("*.*"))