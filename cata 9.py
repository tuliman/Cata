def create_phone_number(n):
    s = ''
    for i in n :
        s+=str(i)
    s = '({}) {}-{}'.format(s[0:3],s[3:6],s[5:len(s)])
    return s




create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
