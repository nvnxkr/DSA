num=12

ans=''

while num>0:
    if num%2==1:
        ans+='1'
    else:
        ans+='0'
    num//=2

ans=ans[::-1]

print(ans)

    