import string
students = [
    ("Alice", 25, 85),
    ("Bob", 22, 90),
    ("Charlie", 25, 90),
    ("David", 22, 85),
    ("Eve", 25, 85),
]
students.sort(key = lambda x: (-x[2] , x[1] , x[0]))
print(students)

sentence = "The quick brown fox jumps over the lazy dog and the fox is quick."
di = {}
sentence = sentence.translate(str.maketrans("","",string.punctuation + string.digits))
words = sentence.lower()
for i in words : 
    if i != ' ' :
        di[i] = di.get(i , 0) + 1
sorted_letters = sorted(di.items() , key = lambda x: (-x[1] , x[0]))
print(sorted_letters[:5])