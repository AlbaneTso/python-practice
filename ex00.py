
import string

di = {}
ls = []
with open ('story.txt') as fhand :
    for line in fhand :
        line = line.rstrip().lower()
        line = line.translate(str.maketrans("", "", string.punctuation + string.digits))
        words = line.split()
        for word in words :
            di[word] = di.get(word, 0) + 1
ls = sorted(di.items(), key = lambda x: -x[1])
print(ls[:5])