nums=[3,4,1,2,5]

mini=float('inf')
smini=float('inf')

for num in nums:
    if num<mini:
        smini=mini
        mini=num
    elif num<smini and num!=mini:
        smini=num
print(smini)