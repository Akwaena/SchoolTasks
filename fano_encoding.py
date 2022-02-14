def encode_symbols(text:str):
    returned = []
    d = {}
    for i in text:
        if i not in '!—,.-?...()—:;«»\nъь':
            d[i] = d.get(i, 0) + 1
    sum_sim = sum(d.values())
    for i in d:
        d[i] = round(d[i] / sum_sim, 3)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    arr = []
    for i in d:
        arr.append(list(i) + [''])


    def func(arr):
        half = sum(map(lambda x: x[1], arr))
        sum1 = 0
        for i, j in enumerate(arr):
            sum1 += j[1]
            if sum1 * 2 >= half:
                index = i + (abs(2 * sum1 - half) < abs(2 * (sum1 - j[1]) - half))
                break

        arr0, arr1 = [], []
        for i in arr[:index]:
            i[2] += '0'
            arr0.append(i)
        for i in arr[index:]:
            i[2] += '1'
            arr1.append(i)

        if len(arr1) == 1:
            returned.append(arr1)
        else:
            func(arr1)
        if len(arr0) == 1:
            returned.append(arr0)
        else:
            func(arr0)


    func(arr)
    return returned


print(encode_symbols(input('>>> ')))
