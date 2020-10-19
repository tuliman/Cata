def next_smaller(n):
    d = 0



    if len(str(n)) != 1:
        for i in range(n - 1, n-len(str(n)), -1):
            print(i)
            if sorted(str(i)) == (sorted(str(n)))  and len(str(i)) == len(str(n)):

                d =i
                print(d)
                return d

    else:
        return -1






print(next_smaller(2017))
