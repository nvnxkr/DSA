def subset(index, valid, res, arr, target, total):
    if index == len(arr):
        if total == target:
            res.append(valid.copy())
        return
    elif total > target:
        return

    valid.append(arr[index])
    total += arr[index]
    subset(index + 1, valid, res, arr, target, total)
    pop = valid.pop()
    total -= pop
    subset(index + 1, valid, res, arr, target, total)


index = 0
valid = []
res = []
arr = [1, 2, 3]
target = 3
total = 0
subset(index, valid, res, arr, target, total)
print(res)
