import numpy as np
from collections import Counter

a = np.array([], dtype=int)
st = ["ATTA", "ACTA", "AGCA", "ACAA"]


for i in st:
    for j in i:
        if j == "A":
            a = np.append(a, 1)
        if j == "C":
            a = np.append(a, 2)
        if j == "G":
            a = np.append(a, 3)
        if j == "T":
            a = np.append(a, 4)


a = a.reshape(4,4)
# qq = []
# for q in range(4):
#     qq.extend(Counter(a[:,q]).most_common(1))
# qwe = []
# for i in qq:
#     for j, v in i:
#        qwe.append(v)

qq = [Counter(a[:,q]).most_common(1) for q in range(4)]
qwe = []
qwe.extend([x[1] for x in a])
www = []
for i in qwe:
    if i == 1:
        www.append("A")
    if i == 2:
        www.append("C")
    if i == 3:
        www.append("G")
    if i == 4:
        www.append("T")
full_data = "".join(www)
print(full_data)
print(a)
print(qq)
# print(Counter(a[:,0]).most_common(1))
print(qwe)
print(www)