import random

print("Rolling the dice...")

num1 = random.randint(1,6)
num2 = random.randint(1,6)

print("Die 1: " + str(num1))
print("Die 2: " + str(num2))
print("Total value: " + str(num1+num2))