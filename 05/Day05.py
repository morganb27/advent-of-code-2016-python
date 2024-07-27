import hashlib

ID = 'ugkcyxxp'

def md5():
    p = ''
    i = 0
    while len(p) < 8:
        s = ID + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h[:5] == '00000':
            p += h[5]
        i+=1
    return p

def md5_2():
    p = [0] * 8
    i = 0
    count = set()
    while len(count) < 8:
        s = ID + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h[:5] == '00000' and h[5].isdigit() and int(h[5]) <= 7 and int(h[5]) not in count:
            index = int(h[5])
            p[index] = h[6]
            count.add(index)
        i+=1
    return ''.join(p)

print(f"Solution to part 1 is: {md5()}")
print(f"Solution to part 2 is: {md5_2()}")