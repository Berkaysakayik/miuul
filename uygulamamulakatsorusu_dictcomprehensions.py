numerics = range(11)
# dictt    = {}
#
# for i in numerics:
#     if i % 2 == 0:
#         dictt[i] = i ** 2
#
# print(dictt)

{i: i**2 for i in numerics if i%2 == 0}