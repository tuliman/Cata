def pr_num(num):
    score = 0
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            score += 1
    if score == 0:
        return num
    else:
        return 1


def gap(g, m, n):
    data = []
    prev = 0
    f = None
    for i in range(m, n):

        if pr_num(i) != 1:



            if i - prev == g:
                return [prev, i]
            prev = i


print(gap(2, 100, 110))
