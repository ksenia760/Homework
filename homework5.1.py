# task N5
n = 0
s = 0
count = 0
min_value = 0
max_value = 0
o = 1
k = 1
while True:
    a = int(input("Enter your number: "))
    if a % 2 == 0:
        o += 1
    if a < min_value:
        min_value = a
    if a > max_value:
        max_value = a

    if a == 0:
        break
    else:
        count += 1
        s += a

print("total: ", count)
print("amount: ", s)
print("arithmetic mean: ", s / count)
print("Min value: ", min_value)
print("Max value: ", max_value)
print("Not even numbers: ", o)
print("Even numbers: ", count - o)


# task N6
n = 50
a = 1
while a**2 <= n:
    print("num 50: ", a**2)
    a = a + 1
    continue

n = 10
a = 1
while a**2 <= n:
    print("num 10: ", a**2)
    a = a + 1
    continue

n = 9
a = 1
while a**2 <= n:
    print("num 9: ",  a**2)
    a = a + 1
    continue

n = 4
a = 1
while a**2 <= n:
    print("num 4: ", a**2)
    a
n = 1
a = 1
while a**2 <= n:
    print("num 1: ", a**2)
    a = a + 1
    continue

n = 100
a = 1
while a**2 <= n:
    print("num 100: ", a**2)
    a = a + 1
    continue

n = 99
a = 1
while a**2 <= n:
    print("num 99: ", a**2)
    a = a + 1





