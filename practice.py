Python lists provide several built-in methods for manipulating data. Below are examples of each requested method: 
#Indexing: Accesses a specific element using its position (starting from 0).
python
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])  # Output: banana



#append(): Adds a single element to the very end of the list.
python
nums = [1, 2, 3]
nums.append(4) 
print(nums)  # Output: [1, 2, 3, 4]



#extend(): Adds all elements from another iterable (like a list) to the end.
python
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)  # Output: [1, 2, 3, 4]


#insert(): Adds an element at a specific index, shifting subsequent items.
python
letters = ['a', 'c']
letters.insert(1, 'b')  # Insert 'b' at index 1
print(letters)  # Output: ['a', 'b', 'c']



#remove(): Deletes the first occurrence of a specific value.
python
items = ['apple', 'banana', 'apple']
items.remove('apple')
print(items)  # Output: ['banana', 'apple']


#pop(): Removes and returns an element at a given index (defaults to the last item).
python
nums = [10, 20, 30]
last = nums.pop()    # Removes 30
first = nums.pop(0)  # Removes 10
print(nums)          # Output: [20]



#count(): Returns the number of times a specified value appears in the list.
python
data = [1, 2, 2, 3, 2]
print(data.count(2))  # Output: 3
