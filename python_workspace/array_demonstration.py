#python code to demonstrate the working of array(), append(), insert()

#importing "array" for array operations
import array
#initialize array with array values
#initialize array with signed integers

arr = array.array('i',[1,2,3])

#printing origin array
print("The new created array is: ",end=" ")
for i in range(0,len(arr)):
    print(arr[i], end=" ")

print("\r")

#using append() to insert new value at end
arr.append(4);

#printing appended ar ray
print("The appended array is: ",end="")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

#using insert() to insert value at specific position
#insert 5 at 2nd position
arr.insert(2,5)

print("\r")

#printing array after insertion
print("The array after insertion is: ",end="")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

print("\r") 

#using pop() to remove elemnt at 2nd position
print("The popped element is: ",end="")
print(arr.pop(2))

#printing array after popping
print("The array after popping is: ",end="")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

print("\r")

#using remove() to remoe 1st occurent of 1
arr.remove(1)

#printing array after removing
print("The arraaty after removing is ",end="")
for i in range(0,len(arr)):
    print(arr[i],end=" ")