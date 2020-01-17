sum = 0
n = 1
while 1 / (2 ** n) > 0.00001:
    sum += 1 / (2 ** n)
    n += 1
print(sum)
