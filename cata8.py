def get_pow(n):
    res = []
    for i in range(1,n):
        for j in range(1,n):
            if i**j==n:
                res.append([i,j])
                return res

def isPP(n):
    res= []
    if type(n)!= list:
        for i in range(1,n):
            for j in range(1,n):
                if i**j==n:
                    res.append([i,j])
    else:
        for f in n:
            res+=(get_pow(f))


    if len(res)!=0:
        return res
    else:
        return None

print(isPP([81,9,4,8,16]))
