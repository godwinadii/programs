lst=[4,2,0,5,1,6,3]
from functools import reduce
print(list(map(lambda num: num**2,lst)))
print(list(filter(lambda num:num>2,lst)))
print(reduce(lambda x,y: x+y,lst))