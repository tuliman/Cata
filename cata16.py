def sum_pairs(ints, s):
    data = []
    prev = None
    prev_2 = None
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                data.append([ints[i], ints[j]])
                if len(data) >= 1 and prev_2 > j:
                    data[0] = [ints[i], ints[j]]
                else:
                    data = data


            prev_2 = j

    print(data)
    if len(data) > 0:

        return (data[0])
    else:
        return None


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
print(sum_pairs(l1, 8))
