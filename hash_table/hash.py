def example(key):
    book = dict();

    book['apple'] = 1.99
    book['milk'] = 9.10

    print(book.get(key))


example('orange')
example('milk')


def n(x):
    return 1


def lengthSTR(s):
    return len(s)


def hash(st):

    mp = dict()

    for i in st:
        print(i, mp)
        mp[i[:1]] = {}
        mp[i[:1]][i] = ''

    return mp

print(hash(['abacate', 'abacaxi', 'bgd']))



