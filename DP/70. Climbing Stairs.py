def func(n):
    if n==0 or n==1:
        return 1

    return func(n-1)+ func(n-2)


ways=func(4)
print(ways)
