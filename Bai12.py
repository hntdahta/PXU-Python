import random

n = random.randrange(50,1000)
print("n =", n)

randomIntList = random.sample(range(-1000,1000),n)
print("List int random =", randomIntList)

randomFloatList =[]
for i in range(0, n):
    x = round(random.uniform(-1000.0, 1000.0), 2)
    randomFloatList.append(x)
print("List float random =", randomFloatList)