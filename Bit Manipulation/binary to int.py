num='11001'

result=0
power=0
for i in range(len(num)-1,-1,-1):
    digit=int(num[i])
    result+=digit * (2**power)
    power+=1

print(result)

