import numpy as np
from collections import Counter

symbols_array = np.array([], dtype=int)
st = ["ATTA", "ACTA", "AGCA", "ACAA"]

for i in st:
    for j in i:
        if j == "A":
            symbols_array = np.append(symbols_array, 1)
        if j == "C":
            symbols_array = np.append(symbols_array, 2)
        if j == "G":
            symbols_array = np.append(symbols_array, 3)
        if j == "T":
            symbols_array = np.append(symbols_array, 4)

symbols_array = symbols_array.reshape(4, 4)

array_column = [Counter(symbols_array[:, q]).most_common(1) for q in range(4)]
most_common_turples = []
most_common_turples.extend([x[0] for x in array_column])
final_list = []

for i in most_common_turples:
    if i[0] == 1:
        final_list.append("A")
    if i[0] == 2:
        final_list.append("C")
    if i[0] == 3:
        final_list.append("G")
    if i[0] == 4:
        final_list.append("T")

final_var = "".join(final_list)
print(final_var)
