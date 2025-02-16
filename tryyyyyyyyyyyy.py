import numpy as np
import pandas as pd
userPrompt = input("Please enter")

if userPrompt == "help":
    print("This tool is useful for managing your AWS resources.")


def sumTwoNumbers(a, b):
    return a + b


def subtractTwoNumbers(a, b):
    return a - b

firstNumber = 3
secondNumber = 2

print(f"The sum of {firstNumber} and {secondNumber} is: {sumTwoNumbers(firstNumber, secondNumber)}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The difference of {a} and {b} is: {subtractTwoNumbers(a, b)}")

matrix = [[1,2],[3,4]]
print(matrix)
matrix2 = [[5,6],[7,8]]
print(matrix2)

result =matrix @ matrix2
print(result)



