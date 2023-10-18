def quickSort(n):
    quickSortHelper(n, 0, len(n) - 1)

def quickSortHelper(n, init, last):
    if(init < last):
        splitPoint = partition(n, init, last)

        quickSortHelper(n, init, splitPoint - 1)
        quickSortHelper(n, splitPoint + 1, last)

def partition(n, init, last):
    pivot = n[init]

    left = init
    right = last

    done = False

    while not done:
        while left <= right and n[left] <= pivot:
            left += 1

        while n[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            n[left], n[right] = n[right], n[left]
    
    n[init], n[right] = n[right], n[init]

    return right

n = [54,26,93,17,77,31,44,55,20]
quickSort(n)
print(n)