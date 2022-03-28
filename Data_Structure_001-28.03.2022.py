from array import *
a = array('i',[1,2,3,4,5])
print("Elements of the array is: ")
for ele in a:
    print(ele)
print(" ")
#APPEND A ELEMENT IN THE ARRAY
a.append(69)
print("Modified Elements are: ")
for ele in a:
    print(ele)
print(" ")
#INSERT AN ELEMENT IN THE ARRAY
a.insert(2,25)
print("Modified Elements are:")
for ele in a:
    print(ele)
print(" ")
#REMOVE AN ELEMENT IN AN ARRAY
a.remove(69)
print("Modified Elements are:")
for ele in a:
    print(ele)
print(" ")
#TO FIND THE POSITION OF AN ELEMENT IN AN ARRAY
n=a.index(3)
print("Position of the element:",n)
#TO REMOVE THE LAST ELEMENT OF THE ARRAY
m=a.pop()
print("Popped Element is:",m)
