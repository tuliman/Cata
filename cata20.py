def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
def even_numbers(num):
    score = 0
    for i in (str(num)):
        if int(i)%2==0:
            score+=1
    return score



def f(n):
    prew = 0
    max_even_num = 0

    for i in range(n - 1, 0, -1):
        if is_prime(i):
            even_numbers(i)
            if even_numbers(i)>prew:

                prew=even_numbers(i)
                max_even_num = i
    return max_even_num




print(f(1000))
