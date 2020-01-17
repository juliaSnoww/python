year = int(input('Enter year '))
if year % 4 != 0:
    print('usual')
elif year % 100 == 0:
    if year % 400 == 0:
        print("high")
    else:
        print("usual")
else:
    print('high')
