def high(x):
    alfavit = sorted(['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'x', 'w', 'y', 'z'])

    val = list(range(1,27))
    data =[]
    alfavit_val = {}

    for i,j in zip(alfavit,val):
        alfavit_val.update({i:j})
    x=list(x.split(' '))
    print(x)

    for f in x :
        data.append([alfavit_val.get(h) for h in f if h in alfavit_val])
    data = ([ g for g in data ] )
    
    return x[data.index(max(data))]


print(high('uwvfasymo rrjzptup'))
