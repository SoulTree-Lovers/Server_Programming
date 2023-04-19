# 1-1 Factorial을 구현하는 함수 factorial을 구현하라.

def factorial(n):
    if n == 1:
        return 1
    
    else:
        return factorial(n-1) * n
    
print(factorial(5))