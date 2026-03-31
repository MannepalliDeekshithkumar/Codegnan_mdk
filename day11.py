'''prime_num = int(input("enter a number"))
count = 0
for j in range(1,prime_num+1):
    print(j)
    if prime_num % j == 0:
        count +=1
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")

for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 2:
        print(f"{an} is a prime number")
    else:
        print(f"{an} is not a prime number")


for so in (1057,197,2,86,17673):
    count = 0
    for j in range(1,so+1):
        if so % j == 0:
            count += 1
    if count == 2:
        print(f"{so} is a prime number")
    else:
        print(f"{so} is not a prime number")



any = [7,2,356,6,3,2,7,6]
empty_ = []
for j in any:
    if j not in empty_:
        empty_.append(j)
        print(empty_)'''


so = 153
length_ = len(str(so))
amstr_ = 0
for j in str (so):
    amstr_ += int(j) ** length_
    print(amstr_)
if amstr_ == so:
    print(f"{so} is a armstrong num")
else:
    print(f"{so} is not a armstrong num")
        





















     
        


























