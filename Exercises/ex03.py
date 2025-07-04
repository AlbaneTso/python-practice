
def factorial(n):
    # print(f"calling factorial {n}")
    if n == 0 :
        return(1)
    return n * factorial(n-1)

# print(factorial(6))

def fibonacci(n):
    # print(f"calling fibo {n}")
    if n <= 1 : return n
    return(fibonacci(n-1) + fibonacci(n-2))

# print(fibonacci(5))

def recursive_sum(lst):
    if len(lst) == 0 : return 0
    return(lst[0] + recursive_sum(lst[1:]))

# print(recursive_sum([4, 5, 6, 7]))
    
def recursive_product(lst):
    if len(lst) == 0: return 1
    return(lst[0] * recursive_product(lst[1:]))

# print(recursive_product([4, 5, 6, 7]))

def recursive_length(s):
    if len(s) == 0 : return 0
    return(1 + recursive_length(s[1:]))

# print(recursive_length("recursion"))

def count_chars(s, c):
    if len(s) == 0 : return 0
    return (s[0]==c) + count_chars((s[1:]), c)

# print(count_chars("abracadabra", "a"))

def is_power_two(n):
    if n <= 0 : return False
    if n == 1 : return True
    if n % 2 != 0: return False
    else : return is_power_two(n // 2)
    
# print(is_power_two(8))

def power(x , n):
    if n == 0 : return 1
    return(x * power(x, n-1))

# print(power(2, 4))