from itertools import combinations


def choose_best_sum(t, k, ls):
    data = 0

    for i in combinations(ls, k):
        if sum(i)<= t:

            data = max(data,sum(i))
            
    if data == 0:
        return None
    return data



xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

print(choose_best_sum(230, 4, xs))
