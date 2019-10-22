import random

for i in range(3):
    print(random.random())
    print(random.randint(4, 13))

member = ["Pedro", "Pedro Luis", "Ana", "Daily"]
boss = random.choice(member)
print(boss)