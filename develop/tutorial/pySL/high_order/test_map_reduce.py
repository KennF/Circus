def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2int(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(fn, map(char2int, s))

def normalize(name):
    return name[0].upper() + name[1:].lower()

if __name__ == '__main__':
    print str2int('1234567')
    print int('1234567')
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
