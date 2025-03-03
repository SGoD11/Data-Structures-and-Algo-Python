# Basic syntax 
x=10
name= 'alice'
is_Studnt = True
print("Basic Syntax")
print(x, name, is_Studnt)


# Type Conversion
num_str = "123"
num_int = int(num_str)
print ("Type conversion")
print(num_str, num_int)
print (type(num_str), type(num_int))

# Control Structure
if x > 5: 
    print("large")
elif x ==5:
    print("small")
else :
    print("small")

#loops
for i in range(5): # 0to 4
    print(i)

#while loop
count = 0
while count < 3:
    print(count)
    count+=1

# Python Data structure
# Lists(Mutable, Ordered)
my_list = [1,2,3]
my_list.append(4)
my_list[0] = 10
print(my_list)
print(len(my_list))
print("My range")
# for i in range(len(my_list)): Retunrs only the index numbers like 0,1,2,3,4
    # print(i) Retunrs only the index numbers like 0,1,2,3,4


# Tuples (Immutable, Ordered)
my_tuple = (1,"apple", True)
print(my_tuple)

#Dictionaries (key value pairs)
my_dict = {
    "Name": "Alice",
    "Place": "Wonderland",
    "age": "21"
}
print(my_dict["Name"] + " in " + my_dict["Place"] )
my_dict["birth"] = "13/11/2003"

# print(my_dict.Name) This gives error

#Sets (Unique ELements)
my_set = {1,2,3}
my_set.add(4)
print(my_set)

# Functions
def add(a,b):
    return a+b

#Lambda func
square = lambda x: x**2
print(square(5))

# Classes and OOP
class Dog:
    def __init__(self, name): # takes an initial param so that it can be used in the descendent functions 
        self.name = name
    def bark(self): 
        print(f"{self.name} says woof!")

d = Dog("Buddy")
d.bark() # Buddy says woof!

# Error Handling
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot be divided by zero")


# List Comprehension (pythonic!)
square = [x**2 for x in range(5)] 
print(square) # [0,1,4,9,16]

## step 2 Transition to DSA with python
# Array/Lists are dynamic

# Example: Reverse a list
array = [1,2,3,4,5]
def reverse_list(arr):
    return arr[::-1] # slicing trick

print(reverse_list(array))

#String
s ="Hello"
print(s[::-1]) # reverse string

#Hash Tables
def find_duplicates(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num,0)+1
        return [k for k, v in counts.items() if v>1]
    

# Stacks & Queues


# stack 
stack = [1,2,3,3,4,5]
stack.append(1) #push 
stack.pop() #pop
print(stack)

# Queue
from collections import deque
# queue = deque() # We can also do this
queue = deque([1,2,3,4,4])
queue.append(1) # enqueue
queue.popleft() # dequeue
print(queue) # output is an array inside a tuple like## deque([])

# Linked Lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Example: 1 -> 2 -> 3
node1 = Node(1)
node2 = Node(2)
node1.next = node2

# print(node1) # <__main__.Node object at 0x000002AD09E616D0>
# print(node2) # <__main__.Node object at 0x000002AD09E60110>
# print(node1.next) # <__main__.Node object at 0x000002AD09E60110>



