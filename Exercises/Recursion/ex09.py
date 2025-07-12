def facons_monter(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return facons_monter(n - 1) + facons_monter(n - 2)



def permutations(chaine):
    if len(chaine) <= 1:
        return [chaine]
    
    resultats = []
    for i in range(len(chaine)):
        lettre = chaine[i]
        reste = chaine[:i] + chaine[i+1:]
        for p in permutations(reste):
            resultats.append(lettre + p)
    return resultats

print(permutations("abc"))
print(facons_monter(4))  