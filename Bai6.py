
import random
randomList = []
n = input("Nhap n = ")
n = int(n)
randomList = random.sample(range(1, 100), n)
max = randomList[0]
for value in randomList:
    if max < value:
        max = value
print("List random:" ,randomList)
print("Max number is:",max)
