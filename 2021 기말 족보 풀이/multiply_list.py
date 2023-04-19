# 1-3 list의 모든 item을 곱하는 함수 multiply_list를 구현하라.

def multiply_list(array):
    num = 1

    for i in array:
        num *= i
    
    return num

print(multiply_list([1, 2, 3, 4]))