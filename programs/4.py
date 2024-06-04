# Write a program to find if the given number is prime or not.

num = int(input("Enter a number: "))

flag = True # set to is prime by default

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = False # set to is not prime
            break

if flag:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")