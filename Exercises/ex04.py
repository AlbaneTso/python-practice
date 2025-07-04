def reverse_strings(s):
    if not s : return s
    return s[-1] + reverse_strings(s[:-1])

# print(reverse_strings("recursion"))

def is_palindrome(s):
    if len(s) <= 1 : return True
    return s[0] == s[-1] and (is_palindrome(s[1:-1]))

# print(is_palindrome("radar"))

def flatten(lst):
    flatten_lst = []
    for item in lst :
        if isinstance(item, list): 
            flatten_lst.extend(flatten(item))
        else : flatten_lst.append(item)
    return(flatten_lst)

# print(flatten([1, [2, [3, 4], 5], 6]))

def count_substring(s, sub):
    if len(s) < len(sub):
        return 0
    if s.startswith(sub):
        return 1 + count_substring(s[1:], sub)
    else: return count_substring(s[1:], sub)
    
# print(count_substring("abababa", "aba"))

def nested_sum(lst):
    total = 0
    if not lst : return 0
    for item in lst :
        if isinstance(item, int) : total+=item
        if isinstance(item, list) : total += nested_sum(item)
    return total

# print(nested_sum([1, [2, [3, 4], 5], 6]))