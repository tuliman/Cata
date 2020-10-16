from itertools import permutations


def next_smaller(n):
    d = 0
    c = ''
    val = []
    st = []
    if len(str(n)) != 1:
        data = (permutations(str(n), len(str(n))))

        for i in data:
            st.append(' '.join(i).replace(' ', ''))
        st = (set([int(x) for x in st if int(x) < n and len(str(x))==len(str(n))]))

        print(val)
        if len(st)!=0:
            return max(st)
        else:
            return -1


    else:
        return -1



print(next_smaller(1234567908))
