a = [0, 4, 'o', 12, 'ok']
b = ['ok', 1, 'b', 'o', 2, 'i']
c = len(set(a) ^ set(b))
print(c)