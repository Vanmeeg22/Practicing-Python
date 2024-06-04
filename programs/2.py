# Write a program to find the given number is positive or negative.

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is a negative number")
elif num > 0:
    print(f"{num} is a positive number")
else:
    print(f"Zero")