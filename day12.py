'''table_num = 8
for j in range(1,50):
    print(f"{table_num} X {j} = {table_num * j}")'''

'''#string:[string is immuatble cant be modified]string is a sequence of character that are enclosed in quotes ['',"","'"']
#example : a = "python"
#          b = "kanna"

#it can be used accessed through index a[0],a[1]'''

'''an = "python is a programming language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
        count_L += 1
print(f"there are total {count_U} Cap L")
print(f"there are total {count_L} Small L")


an = "python is a programming language"
Cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f" {Cap_L} contain all Cap L")
print(f"{small_L}conatain all  Small L")


UBI_kanna_ac_details = {"name": "kanna",
                        "atm pin":"9999"}
print("welcome to UBI atm")
print("please insert your atm card")
UBI_user_pin = input("pls enter your 4digits atm pin")
if len(UBI_user_pin) == 4:
    if UBI_user_pin in UBI_kanna_ac_details['atm pin']:
        print("hai")

UBI_kanna_ac_details = {"name": "kanna",
                        "atm pin":"9999"}
print("welcome to UBI atm")
print("please insert your atm card")
UBI_user_pin = input("pls enter your 4digits atm pin: ")
if len(UBI_user_pin) == 4:
    if UBI_user_pin in UBI_kanna_ac_details['atm pin']:
        print("the pin correct")
    else:
        print("you have entered invalid pin")
else:
    print("pls enter 4 digit pin")'''


per_num = int(input("enter a number"))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
         fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")









































