from array import *
a = [[1,2,3,4,5],[6,7,8,9,0]]
print("The elements are: ")
for ele in a:
    print(ele)
#To access a particular row in the array
print("Access the particular element in the array;")
print(a[0])
#To access a particular element in the array
print("Access the particular row in the array;")
print(a[1][1])
#Insert an element in the array
print("Array after inserting the element")
a.insert(1,[100,200])
for r in a:
    for c in r:
        print(c,end=" ")
        print()
#Delete the element in the array
print("Array after deletion")
del(a[1])
for r in a:
    for c in r:
        print(c,end=" ")
        print()
#Array after updating
print("Array after updating")
a[1]=[10,20,30]
a[0][1]=11
for r in a:
    for c in r:
        print(c,end=" ")
        print()


