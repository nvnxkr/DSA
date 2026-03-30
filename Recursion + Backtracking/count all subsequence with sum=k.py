def subsequence(i, arr, sum, target, count):
    if i == len(arr):
        if sum == target:
            return 1
        return 0

    if sum > target:
        return 0

    sum = sum + arr[i]
    pick = subsequence(i + 1, arr, sum, target, count)
    sum = sum - arr[i]
    not_pick = subsequence(i + 1, arr, sum, target, count)
    return pick + not_pick


result = subsequence(0, [1, 2, 3], 0, 3, 0)

print(result)
