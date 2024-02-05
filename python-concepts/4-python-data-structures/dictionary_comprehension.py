keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
dic1 = {k: v for (k, v) in zip(keys, values)}
print("Dict1 :", dic1)

dic2 = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print("Dict2 :", dic2)

dic3 = {x.upper(): x * 3 for x in 'coding '}
print("Dict3 :", dic3)

dic4 = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print("Dict4 :", dic4)
