import random

SetA = {1,2,3,4,5}
#print(SetA[0])
#that Sets are not indexable
SetA.add(6)

SetA.remove(1)
#Set Operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference
print(SetA)
SetB = {4,5,7,8,9,10}
print(SetA|SetB)
print(SetA&SetB)
print(SetA-SetB)
print(SetA^SetB)