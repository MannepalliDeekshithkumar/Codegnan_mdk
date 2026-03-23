'''
if statement --> this (is statement) is used to check any condition, if the condition
becomes true then it will enter in side the (if statement)'''
'''age = int(input("enter your age"))
if age >= 18:
    print("print your age or above")'''
'''student_att = int(input("pls enter your sem attendace:")
if student_att >= 18:
    print("you can directly sit in sem exam")
    '''
'''#if-else statements--> this also called as fall back statement
#which only execute when the (is statement) become false

age = int(input("enter your age:"))
if age >= 18:
    print("you can vote")
else:
    print(f"you can not and have to wait {18-age} years")


total_amount = int(input("enter the total shopping money:"))
if total_amount >=150:
    print("no deliver cost")
else:
    print(f"add {150 - total_amount} to your cart")
    

total_fees = int(input("enter the total fees:"))
if total_fees >=10000:
    print(" extra fine")
else:
    print(f"minus {10000 + total_fees} to your college:")'''

'''#if-elif-else statement (if + else)--- in the elif part,i can more conditiom
    
student_marks = int(input("enter your marks:"))
if student_marks >= 90:
    print("you got A+ grade")
elif student_marks >= 75 and student_marks <90:
    print("you got a grade")
elif student_marks >=60 and student_marks <75:
    print("you got b grade")
else:
    print("your fail")
# user caluculator


num_1 = int(input("enter 1st number:"))
num_2 = int(input("enter 2nd number:"))
user_choice =(input("enter your choice:"))
if user_choice =="+":
    print(num_1 + num_2)
elif user_choice == "-":
    print(num_1 - num_2)


num_1 = int(input("enter 1st number:"))
num_2 = int(input("enter 2nd number:"))
user_choice = (float(input("enter your choice\n1.Add \n2.Sub \n3.Multiply \n4.divide")))
if user_choice == 1:
    print(num_1 + num_2)'''

user_choice = int(input("pls enter any number:"))
if user_choice % 2 == 0:
    print(f"{user_choice} is a even number")
else:
    print(f"{user_choice} is a odd number")






















