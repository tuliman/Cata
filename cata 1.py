def anagrams(word, words):
    data = []
    word = sorted(list(word))
    for i in words:
        if word == sorted(i):
            data.append(i)
    return data












print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
