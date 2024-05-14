def ShellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = [12, 34, 54, 2, 3]
ShellSort(arr)
print("Lista ordenada con ShellSort:", arr)



def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

arr = [12, 34, 54, 2, 3]
sorted_arr = QuickSort(arr)
print("Lista ordenada con QuickSort:", sorted_arr)



def Heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

def HeapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        Heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

arr = [12, 34, 54, 2, 3]
HeapSort(arr)
print("Lista ordenada con HeapSort:", arr)



def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        countingSort(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print("Lista ordenada con RadixSort:", arr)

