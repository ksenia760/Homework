# task N10
a = input().split()
s = 0
for i in range(1, len(a)-1):
    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]):
        s += 1
print(s)

# task N11
a = [int(n) for n in input().split()]
k = int(input())
for i in range(k, len(a) - 1):
    a[i] = a[i + 1]
a.pop()
print(" ".join([str(i) for i in a]))