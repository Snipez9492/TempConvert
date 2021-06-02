"""
Write a program that converts temperature in different countries.
"""

# print("This is the first commit.")


def fahrenheit_to_celsius(degree):
    ans = ((degree - 32) * 5 / 9)
    return ans


response = int(input("What is the degrees in fahrenheit: "))

print("In celsius it will convert to " + str(fahrenheit_to_celsius(response)))
