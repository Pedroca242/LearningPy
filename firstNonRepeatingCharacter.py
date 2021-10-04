def noRepeat(p):
    r = {}
    for i in p:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    for j, k in r.items():
        if k == 1 and j != " ":
            return j
    return "_"

palavra = "aabb bacd"

print(noRepeat(palavra))
