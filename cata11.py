def sum_of_intervals(intervals):
    data = []
    f = set()

    intervals=(list(set(intervals)))
    data = ([(list(range(i[0],i[1]))) for i in intervals])
    for d in data:
        for j in d :
            f.add(j)
            print(f)
    return len(f)







print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
