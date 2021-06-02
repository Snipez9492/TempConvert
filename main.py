"""
Write a program that converts temperature in different countries.
"""


# print("This is the first commit.")


def fahrenheit_to_celsius(degree):
    ans = ((degree - 32) * 5 / 9)
    return ans


def celsius_to_fahrenheit(degree):
    ans = ((degree * 9 / 5) + 32)
    return ans


response = int(input("What is the degrees in fahrenheit: "))

print("In celsius it will convert to " + str(fahrenheit_to_celsius(response)))

response1 = int(input("What is the degrees in celsius: "))

print("In fahrenheit it will convert to " + str(celsius_to_fahrenheit(response1)))
