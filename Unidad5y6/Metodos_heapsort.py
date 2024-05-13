def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print("Paso 1:", arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        print("Paso", n - i + 1, ":", arr)


arr = [741, 200, 21, 4371, 32, 42, 21, 17, 0, 10, 1741, 231, 59, 62, 41, 62,41, 23, 111110, 0024, -27]
print("Arreglo original:", arr)
heap_sort(arr)
print("Arreglo ordenado:", arr)