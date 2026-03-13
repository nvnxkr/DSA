result = []


def sol(i, flag, current, n=3):
    if len(current) == n:
        result.append(current)
        return

    if flag == True:
        sol(i + 1, True, current + "1")
        sol(i + 1, False, current + "0")
    else:
        sol(i + 1, True, current + "1")


sol(0, True, "")
print(result)
