


def count_change(money, coins):
    if money == 0:
        return 1
    if money < 0:
        return 1
    c = 0
    for i in range(len(coins)):
        c=count(money,coins[i])
        print(c)

    return c

print(count_change(4, [1, 2]))
