def prime_check(number):
    divisible = 0
    for i in range(2, number):
        if number % i == 0:
            divisible += 1
    
    if divisible == 2:
        print("Its a prime number")
    else: 
        print("Its not a prime number")

while True:
    n = int(input())
    if n > 100:
        n = int(input())
    else:
        prime_check(number=n)
        break

