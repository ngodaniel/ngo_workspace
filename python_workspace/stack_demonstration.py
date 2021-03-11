# Python program to demonstrate stack implementation using list

stack = []

#append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("initial stack")
print(stack)

#pop() function to pop lement from stack in LIFO
print("\nElements popped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nSta ck after elements are popped: ")
print(stack)
