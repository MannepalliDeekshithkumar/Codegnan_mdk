'''vowel_con = input("enter a letter:")
if vowel_con in "aeiouAEIOU":
    print("vow")
else:
    print("con")


Time_aday = input("enter 24 hours time:")
parts_ = Time_aday.split(":")
hours_ = int(parts_[0])
Min_ = int(parts_[1])
if hours_ >=13 and Min_ < 60:
    print(f"{Time_aday} convert into {hours_- 12}:{Min_}pm")
else:
    print(f"you have entered nrml or main are incorrect")'''
    


#LIST---> COLLECTION OF DIFFERENT ITEMS INSIDE THE [] , WHICH ARE SEPARATED BY(,)
#EG---> [1,"NAME",[1,2,"DEEKSHITH"]]

'''list_1 = [1,2,3,"coding",[1,2,["coding","language"],"computer"]]
print(list_1[4][2][0][4])


list_2 = [2,3,4,"java",[1,2,["code","python"],"java"]]
print(list_2[4][2][1][2])'''

#METHODS OF LIST
#APPEND()---> THIS METHOD IS USED TO ADD NEW ITEMS INTO LIST IT WILL ONLY GO FOR
#THE LAST INDEX OF THE LIST
#EX-->list_3 = [1,2,3,4]
#(list_2)
#list_3.append(67)
#print(list_3)--->(OUTPUT:1,2,3,4,67)

#MUTABLE---> I CAN DIRECTLY MODIFY ON THAT PARTICULAR VARIABLE
#IMMUTABLE---> I CAN NOT NODIFY DIRECTLY ON THE VARIABLE
#SYNTAX:Variable_name.append(item)



#EXTEND()---> THIS METHOD IS USED TO ADD ITEMS TO LIST IN THE
#SYNTAX:variable_name.extend("item")
'''list_1 = [7,18,8,25]
list_1.extend("kanna")
print(list_1)--->[7, 18, 8, 25, 'k', 'a', 'n', 'n', 'a']'''


#REMOVE()---> this method will delete directly the item or a value.
#SYNTAX:variable_name.remove(item)
'''list_4 = [23,76,66,"kanna"]
list_4.remove("kanna")
print(list_4)---->[23, 76, 66]'''

#POP()--->THIS METHOD WILL DELETE THE ITEM OR VALUE BASED ON INDEX POSITION
#SYNTAX:VARIABLE_NAME.POP(INDEX VALUE)
list_1 = [22,22,"java"]
list_1.pop(2)
print(list_1)
























































