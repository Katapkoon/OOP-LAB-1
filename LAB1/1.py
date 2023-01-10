for x in range(2000,3201):
    if x % 7 == 0 and not x % 5 == 0:
        print(str(x) + ',', end='')
    else:
        continue
    