hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
requests = [[0, 3], [3, 7], [14, 18], [19, 22], [22, 24]]
requests.sort()
trouble_requests = []


def req():
    for i in requests:
        for j in range(i[0], i[1] + 1):
            if j in hours:
                hours.remove(j)


def trouble():
    a = 1
    for i in range(0, len(requests) - 1):
        if requests[0][1] > requests[a][0] and requests[0][1] != requests[a][0]:
            trouble_requests.append(requests[i])

        a += 1

req()
trouble()

print("Свободные часы:")
print(hours)
print("Пересекающиеся заявки:")
print(trouble_requests)
