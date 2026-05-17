# ============================================================
# CDPC DSA Training – Day 4
# Topic: Sorting Algorithms
# Language: Python
# ============================================================


# ------------------------------------------------------------
# Bubble Sort – Ascending Order
# ------------------------------------------------------------

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    bubblesort(arr)
    print(*arr)


# ------------------------------------------------------------
# Bubble Sort – Descending Order
# ------------------------------------------------------------

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    bubblesort(arr)
    print(*arr)


# ------------------------------------------------------------
# Selection Sort – Ascending Order
# ------------------------------------------------------------

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[i]
        loc = i
        for j in range(i + 1, n):
            if min > arr[j]:
                min = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selectionsort(arr)
    print(*arr)


# ------------------------------------------------------------
# Selection Sort – Descending Order
# ------------------------------------------------------------

def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        max = arr[i]
        loc = i
        for j in range(i + 1, n):
            if max < arr[j]:
                max = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selectionsort(arr)
    print(*arr)


# ------------------------------------------------------------
# Insertion Sort – Ascending Order
# ------------------------------------------------------------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i - 1

        while pos >= 0 and current < arr[pos]:
            arr[pos + 1] = arr[pos]
            pos = pos - 1

        arr[pos + 1] = current

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    insertion_sort(arr)
    print(*arr)


# ------------------------------------------------------------
# Insertion Sort – Descending Order
# ------------------------------------------------------------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i - 1

        while pos >= 0 and current > arr[pos]:
            arr[pos + 1] = arr[pos]
            pos = pos - 1

        arr[pos + 1] = current

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    insertion_sort(arr)
    print(*arr)
