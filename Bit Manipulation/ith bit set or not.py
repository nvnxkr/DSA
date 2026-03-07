n=13
i=0


# By LEFT Shift
'''

i=1<<i

num= n&i

if num==0:
    print('false')

else:
    print("True")

'''

# By RIGHT Shift

n=n>>i

if n&1 !=0:
    print("true")
else:
    print("false")


