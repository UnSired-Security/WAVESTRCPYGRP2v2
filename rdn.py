import random as r
list = [1,1,2,3,2,3,4,5,6,6]
r.shuffle(list)
for x in list:
    for y in list:
        result = (f"{x} : {y}")
        print(result)
