def sum_for_list(lst):
    data = []
    end_lst = []
    for i in lst:
        for j in range(2, i // 2):
            if i % j == 0 and j % 2 != 0 or j == 2:
                data.append(j)

    data = list(set(data))




sum_for_list([12, 15])
