


n = int(input("Enter number:"))
length = len(str(n))
rev = 0
for i in range (length):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print(rev)



