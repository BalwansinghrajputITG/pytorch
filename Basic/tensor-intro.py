import torch as t
# print pytorch version
print(t.__version__)

# create a tensor
x = t.tensor([1,2,3,4,5])

# print(x) .  convert x to float before calculating mean
m = t.mean(x.float())

# print(m)

# create a tensor with specific data type
y = t.tensor([1,2,3,4,5], dtype=t.float32)
# print(y)

# create a 2D tensor
m2 = t.tensor([
    [1,4] , [1,2] , [1,2] , [1,2] , [1,2]
])

# print(m2)

# create a tensor of zeros, ones and random values
z = t.zeros((2,3))
# print(z)

o = t.ones((2,3))
# print(o)

r = t.rand((2,3))
# print(r)