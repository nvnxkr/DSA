arr = [1, 2, 3, 4, 5, 6, 7]


def heapify(arr, ind):
    curr = ind

    left = 2 * ind + 1
    right = 2 * ind + 2

    if left < len(arr) and arr[curr] < arr[left]:
        curr = left
    if right < len(arr) and arr[curr] < arr[right]:
        curr = right

    if curr != ind:
        arr[curr], arr[ind] = arr[ind], arr[curr]
        heapify(arr, curr)


heapify(arr, 0)
print(arr)
