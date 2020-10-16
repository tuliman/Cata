def next_smaller(n):
    d = 0
    


    if len(str(n)) != 1:
        for i in range(n - 1, n - int(str(n)[1::]), -1):
            if sorted(str(i)) == (sorted(str(n)))  and len(str(i)) != len(str(n)):
                d =1
                print(d)
                return d

    else:
        return -1






print(next_smaller(907))
