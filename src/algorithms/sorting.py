def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr.swap(j, j + 1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr.swap(i, min_idx)

def quick_sort(arr):
    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr.swap(i, j)
        arr.swap(i + 1, high)
        return i + 1
    
    _quick_sort(0, len(arr) - 1)

def merge_sort(arr):
    def _merge_sort(l, r):
        if l < r:
            m = (l + r) // 2
            _merge_sort(l, m)
            _merge_sort(m + 1, r)
            merge(l, m, r)
    
    def merge(l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [arr[l + i] for i in range(n1)]
        R = [arr[m + 1 + j] for j in range(n2)]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    _merge_sort(0, len(arr) - 1)

def heap_sort(arr):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr.swap(i, largest)
            heapify(n, largest)
    
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr.swap(0, i)
        heapify(i, 0)

def shell_sort(arr):
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
