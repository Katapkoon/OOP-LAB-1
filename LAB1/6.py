n = input('Enter number : ')

list1 = []
for i in range(int(n),0,-1):
    list1.append(' '*i + '#'*(2+(int(n)-1)-i))
print('\n'.join(list1))