'''
    리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오.
    data =[7,1,5,9,3,2,4]
    3
'''
data =[7,1,5,9,3,2,4]
print(data.index(2))

def max_index(list):
    max=-100
    for num in list:
        if num > max:
            max = num
    print(list.index(max))

max_index(data)     

def find_index_largest(data):
    largest_index = 0
    for i in range(len(data)):
        # 더 큰 값을 찾은 경우 
        if data[largest_index] < data[i]:
            largest_index = i
    return largest_index

largest_index = find_index_largest(data)
print(largest_index)

'''
    특정한 값을 가지는 원소의 인덱스를 찾는 함수를 작성해 보시오.
    [3,5,7,9], 2    => -1 리턴
    [3,5,7,9], 7    => 2

    enumerate()
'''
# for a in enumerate([3,5,7,9]):
#     print(a)
#     print(a[0])

print()
list=[3,5,7,9]
def index_return(list, val):
    result=-1
    for a in enumerate(list):
        if val == a[1]:
            result = a[0]
    return result

print(index_return(list,2))
print(index_return(list, 7))

print()


def find_specific_value(lis,value):
    for i , x in enumerate(lis):
        if x == value:
            return i
    return -1   # 찾지 못한 경우

print(find_specific_value(list, 2))
print(find_specific_value(list, 7))
print(find_specific_value([23,15,27,19], 19))

'''
    하나의 자연수가 주어졌을 때, 소수인지 아닌지 판별하는 함수를 작성하시오.

'''
def prime_num_tf(num):
    # 1 이하인 경우 소수가 아님
    if num <= 1:
        return False
    # 1과 자기 자신 외의 자연수로 나누어지면 소수가 아님
    for x in range(2, num):
       if num % x== 0:
            return False
    return True

print()
print(prime_num_tf(17))
print(prime_num_tf(22))
print(prime_num_tf(4))
print(prime_num_tf(74))
