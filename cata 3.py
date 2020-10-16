def tickets(people):
    ticket = 25
    cash = 0
    cash_50 = 0
    if people[0] - ticket == 0:
        cash += 1

        for i in range(1, len(people)):
            if people[i] == ticket:
                cash += 1
            elif people[i] == 50 and cash >= 1:
                cash -= 1
                cash_50 += 1

            elif people[i] == 100:
                if (cash_50 >= 1 and cash >= 1):
                    cash_50 -= 1
                    cash -= 1
                elif cash >= 3:
                    cash -= 3
                else:
                    return 'NO'
            else:
                return 'NO'
    else:
        return 'NO'
    if cash < 0 and cash_50 < 0:
        return 'No'
    else:
        return 'YES'


print(tickets([25, 25, 50, 100]))
