# arr=[1,2,3,4,5,6,7,8,9,10,1,2]
# from collections import Counter
# freq=Counter(arr)

# print(freq)

# print(freq.most_common(2))

from itertools import product
import itertools
print([''.join(i) for i in product(['0','1'],repeat=2)])

print(dir(itertools))