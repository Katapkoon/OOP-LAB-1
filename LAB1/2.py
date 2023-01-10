word = input("Enter a string: ")
upperCases = []
lowerCases = []

for x in word:
    if x.isupper():
        upperCases.append(x)
    else:
        lowerCases.append(x)

print('Uppercases :'+ str(len(upperCases)))
print('Lowercases :'+ str(len(lowerCases)))