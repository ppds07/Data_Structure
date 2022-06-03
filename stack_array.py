s=[]

def empty(s):
    return len(s) == 0

def push(s,item):
     s.append(item)
     print(item,"pushed inside the stack")

def pop(s):
    n=s.pop()
    print(n,"popped from the stack")

def peek(s):
    print("Elements in stack: ")
    for i in s:
        print(i,end=" ")


push(s, str(10))
push(s, str(20))
push(s, str(30))
pop(s)
peek(s)
print()
n=len(s)
print("Top Element: ", s[n-1])
