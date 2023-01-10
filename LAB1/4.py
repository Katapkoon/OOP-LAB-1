a = input("Enter your number : ")
sum = 0
i = 1
while(i <= 4):
    temp = str(a) * i
    sum += int(temp)
    i += 1
print(sum)
