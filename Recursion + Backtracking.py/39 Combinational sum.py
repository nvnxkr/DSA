def combinational(arr, target):
    sub = []
    result = []
    sum = 0

    def solve(ind, sub, res, arr, target, sum):

        if sum == target:
            result.append(sub.copy())
            return
        if sum > target or ind == len(arr):
            return

        sub.append(arr[ind])
        sum = sum + arr[ind]
        solve(ind, sub, res, arr, target, sum)
        sub.pop()
        sum = sum - (arr[ind])
        solve(ind + 1, sub, res, arr, target, sum)

    solve(0, sub, result, arr, target, sum)

    return result


arr = [2, 3, 6, 7]
target = 7

print(combinational(arr, target))
