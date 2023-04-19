# 1-2 문자열의 길이를 구하는 함수 string_length를 구현하라.

def string_length(string):
    length = 0

    for i in string:
        length += 1

    return length

print(string_length("orange"))