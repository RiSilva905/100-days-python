# Check for first 100 numbers if is a prime number
is_prime = True
n = int(input("Write a number between 1 and 100 to check if it's prime: "))

for i in range (2, n):
    if n % i == 0:
        is_prime = False
if n == 1:
    is_prime = False
if is_prime:
    print(f"The number", n, "is a prime number")
else: 
    print(f"The number", n, " is not a prime number")