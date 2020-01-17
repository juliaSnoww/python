spaceCount = int(input('Enter tree size '))
level = 1
while spaceCount > 0:
    asteriskCount = (level * 2) - 1
    print(' ' * spaceCount + '*' * asteriskCount)
    spaceCount -= 1
    level += 1
