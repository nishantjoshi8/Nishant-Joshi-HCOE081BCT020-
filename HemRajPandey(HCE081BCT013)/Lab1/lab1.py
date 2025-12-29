# Lab 1 Assignment

# 1. Draw a sine wave using matplotlib for x from 0 to 2π
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)   # 100 points between 0 and 2π
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave from 0 to 2π")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()


# 2. Function-based Python program to compute factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print("Factorial of 5 is:", factorial(5))


# 3. Print all prime numbers between 1 and 100
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers between 1 and 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")