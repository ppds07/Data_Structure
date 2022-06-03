def part(a, min, max):
    pivot = a[max]
    i = min - 1
    for j in range(min, max):
        if a[j] <= pivot:
            i = i + 1
            (a[i], a[j]) = (a[j], a[i])
    (array[i + 1], a[max]) = (a[max], a[i + 1])
    return i + 1


def quicksort(a, min, max):
    if min < max:
        sub_a = part(a, min, max)
        quicksort(a, min, sub_a - 1)
        quicksort(a, sub_a + 1, max)
        
array = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(array)
n = len(array)
quicksort(array, 0, n-1)
print('Sorted Array in Ascending Order: ')
print(array)
