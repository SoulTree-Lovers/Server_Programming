# 1-4 dictionary에서 key가 존재하는지 체크하는 함수 
# is_key_present를 구현하라.

def is_key_present(dictionary, key):
    is_key = False

    for i in dictionary:
        if key == i:
            is_key = True

    return is_key

dictionary = {"key1": "value1", "key2": "value2"}

print(is_key_present(dictionary, "key1"))
print(is_key_present(dictionary, "key3"))