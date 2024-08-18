import random

def generate_random_prime(lower, upper):
    while True:
        num = random.randint(lower, upper)
        if check_prime(num):
            return num

# def check_prime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

def check_prime(num):
    i = 2
	
    while i < num:
        R = num % i
        if R == 0:
            return False
        i += 1
    else:
        return True
    
#print(generate_random_prime(1, 10000))