s = input("Enter ")
a = ""
i = len(s) - 1
while s[i] != '/':
    i = i-1
i = i+1
while s[i] !='.':
    a = a + s[i]
    i = i + 1
print(a)

