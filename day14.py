'''for j in range(num):
    for i in range(j):
        print(j,end = "")
    print()
    
1
22
333
4444

num =int(input("Enter the limit: "))
for j in range(1,num+1):
    for i in range(num+1):
        print("*",end = " ")
    print()
    
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * *
    

num =int(input("Enter the limit: "))
for j in range(1,num-1):
    for i in range(num-1):
        print("*",end = " ")
    print()
    
* * * * * 
* * * * * 
* * * * * 
* * * * *


num =int(input("Enter the limit: "))
for j in range(num):
    for i in range(num-j):
        print("*",end = " ")
    print()
    
* * * * * 
* * * * 
* * * 
* * 
* '''


'''num =int(input("Enter the limit: "))
for j in range(num):
    for i in range(num-1):
        print("*",end = " ")
    print()

n = int(input("Enter the limit: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
*
* * 
* * * 
* * * * 
* * * * *


num = int(input("enter the limit:"))
for j in range(num):
      print(" " *(num - j), end = "")
      for i in range(j+1):
        print("*", end = " ")
      print()
          


         * 
        * * 
       * * * 
      * * * * 
     * * * * * 
    * * * * * * 
   * * * * * * * 
  * * * * * * * * 
 * * * * * * * * * 



num = int(input("enter the limit:"))
for j in range(num):
      print(" " *(num - j), end = "")
      for i in range(j+1):
        print("*", end = " ")
      print()'''



ICIC_teja_AC_details = {"Name" : "Sunny",
                        "ATM PIN" : "0066",
                        "Balance" : 100000}
print("WELCOME TO ICIC ATM")
print("PLS INSERT YOUR ATM CARD")
ICIC_user_pin = input("pls enter 4 digits ATM pin: ")
if len(ICIC_user_pin) == 4:
    if ICIC_user_pin in ICIC_teja_AC_details['ATM PIN']:
        user_choice = int(input("Enter \n1.withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw: "))
            if money_w <= ICIC_teja_AC_details['Balance']:
                ICIC_teja_AC_details['Balance'] -= money_w
                print(ICIC_teja_AC_details['Balance'])
            else:
                print("insuff")
        else:
            print("you have entered invalid pin")
else:
    ("pls enter 4 digit pin ")




























































