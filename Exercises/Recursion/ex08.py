def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
    

def generate_binary(n):
    if n == 0:
        return ['']
    smaller = generate_binary(n - 1)
    return ['0' + bit for bit in smaller] + ['1' + bit for bit in smaller]

def sum_tree(tree):
    total = 0
    for value in tree.values():
        if isinstance(value, dict):
            total += sum_tree(value)
        elif isinstance(value, int):
            total += value
    return total

print(sum_digits(1234))
print(generate_binary(3))
print(sum_tree(tree = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    },
    'f': 4
}
))