'''
    * 텐서(tesnor)
        - 베열(array)이나 행렬(matrix)과 매우 유사한 특수한 자료구조
'''
from builtins import print

#list로부터 tensor 생성하기

import torch
import numpy as np

data = [[1,2], [3,4]]
x_data = torch.tensor(data)
print(x_data)

# numpy array로부터 tensor 생성하기 -- copy본으로 생성
np_array = np.array(data)
x_np_1 = torch.tensor(np_array)
print(x_np_1)

x_np_2 = torch.as_tensor(np_array)  # view를 만듬 . 오리지널 데이터 사용
print(x_np_2)

x_np_3 = torch.as_tensor(np_array)  # view를 만듬
print(x_np_3)

x_np_4 = torch.as_tensor(np_array)  # view를 만듬
print(x_np_4)


x_np_1[0,0] =5
print(x_np_1)
print(x_np_2)
print(x_np_3)

print("---------------------")
np_again = x_np_1.numpy()
print(np_again, type(np_again))

print("------")
a=torch.ones(2,3)
print(a)

b= torch.zeros(2,3)
print(b)

c= torch.full((2,3),2)
print(c)

d= torch.empty(2,3)
print(d)

print("---------------------")
e= torch.arange(10)
print(e)

f= torch.rand(2,2)
print(f)

g= torch.randn(2,2)
print(g)

print(f"Shape of tensor : {f.shape}")
print(f"Datatype of tensor : {f.dtype}")
print(f"Device tensor is stored on : {f.device}")

print("-----------------------------")
a= torch.arange(1,13).reshape(3,4)
print(a)

#indexing
print(a[1])
print(a[0,-1])

#slicing
print(a[1:-1])
print(a[:2, 2:])    # 첫 번째 행, 두 번째 행까지의 모든 행과 세 번째 이후의 모든 열

print("---------------------------")
x = torch.tensor([[1,2],[3,4]], dtype=torch.float32)
y= torch.tensor([[5,6],[7,8]], dtype= torch.float32)

print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x@y)
print('='*30)
print(torch.add(x,y))
print(torch.subtract(x,y))
print(torch.multiply(x,y))
print(torch.divide(x,y))
print(torch.matmul(x,y))


# in-place 연산
print(x.add(y))
print()