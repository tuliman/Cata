def last_digit(n):
    n = sum(list([i for i in range(n+1)]))
    print(n)
    for f in str(n):
        if f !='0':
            return int(f)








print(last_digit(12))
