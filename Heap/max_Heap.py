class Max_heap:
    def __init__(self):
        self.arr = []
        self.cnt = 0

    def heapify_down(self, arr, ind):
        largest = ind

        left = 2 * ind + 1
        right = 2 * ind + 2

        if left < len(arr) and arr[left] > arr[largest]:
            largest = left

        if right < len(arr) and arr[right] > arr[largest]:
            largest = right

        if largest != ind:
            arr[largest], arr[ind] = arr[ind], arr[largest]
            self.heapify_down(arr, largest)

    def heapify_up(self, arr, ind):
        parent = (ind - 1) // 2
        if ind > 0 and arr[ind] > arr[parent]:
            arr[ind], arr[parent] = arr[parent], arr[ind]
            self.heapify_up(arr, parent)

    def heapify(self, arr, ind, val):
        if arr[ind] > val:
            arr[ind] = val
            self.heapify_down(arr, ind)
        else:
            arr[ind] = val
            self.heapify_up(arr, ind)


heap = Max_heap()
heap.arr = [10, 9, 8, 7, 6]
heap.heapify(heap.arr, 0, 5)
print(heap.arr)
