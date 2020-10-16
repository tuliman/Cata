def pairwise(arr, n):
    s = arr

    data = list()

    for i in range(len(s)):
        for j in range(i + 1, len(s)):

            if s[j] != s[i] and s[i] + s[j] == n:
                data.append(i+j)
                print(data)

    return


print(pairwise([0, 0, 0, 0, 1, 1], 1))
