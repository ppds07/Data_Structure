stack=[]

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
     stack.append(item)
     print(item,"pushed inside the stack")

def pop(stack):
    n=stack.pop()
    print(n,"popped from the stack")

def peek(stack):
    print("Elements in stack: ")
    for i in stack:
        print(i,end=" ")


push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack))
peek(stack)
print()
n=len(stack)
print("Top Element: ", stack[n-1])
