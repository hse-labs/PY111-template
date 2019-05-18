def shitalochka(n, k):
    n2 = [i for i in range(1, n + 1)]
    i = 0
    j = 0
    c = 0
    while len(n2) > 1:
        if i >= len(n2) + c:
            i = 1
            j += 1
            c = 0
        else:
            i += 1
            j += 1
        if j == k:
            del n2[i-1-c]
            j = 0
            c += 1
    return n2


def dnaread(n):
    concensus = ""
    for i in range(len(n[0])):
        d = {}
        for j in range(len(n)):
            if n[j][i] in d:
                d[n[j][i]] += 1
            else:
                d[n[j][i]] = 1
        count = 0
        p = None
        for k in d:
            if d[k] > count:
                count = d[k]
                p = k
        concensus += p
    return concensus


if __name__ == "__main__":
    print(dnaread(("FAVGH", "GARGO", "FALGI", "CAROO")))
