# 1. 사용자로 부터 comma seprated 입력 문자열을 받아서, list와 tuple을 만들어 출력하시오

#  coding here
# split(',')를 통해 comma 구분자로 문자열을 나누어 입력받는다.
string = input("Input some comma separated numbers : ").split(',')
comma_separated_string_to_list = list(string)
comma_separated_string_to_tuple = tuple(string)

print(comma_separated_string_to_list)
print(comma_separated_string_to_tuple)
# Console Output
# ---------------------------------------------
# Input some comma seprated numbers : 3,5,7,23
# List :  ['3', '5', '7', '23']
# Tuple :  ('3', '5', '7', '23')


# 2. 사용자로부터 input 숫자 n을 입력받아 n+nn+nnn을 계산하여 출력하시오
#    예를 들면, 입력숫자가 5인 경우 5+55+555로 계산되어 615값을 출력함

#  coding here
# 문자열로 입력 받은 후, 문자열 덧셈 연산 이후 int() 함수를 통해 수로 바꾸어 계산한다.
n = input("Input an integer : ")
n1 = int(n)
n2 = int(n+n)
n3 = int(n+n+n)

print(n1+n2+n3)


# Console Output
# ---------------------------------------------
# Input an integer : 5
# 615


# 3. 아래 numbers list에서 짝수인 원소만 출력하시오.
#    단, 원소의 값이 237이면 list의 다음 원소값을 읽지 말고 출력을 멈추시오(for-loop에서 break)

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]


#  coding here
# numbers를 반복하며 237 발견 시 break한다.
# num을 2로 나눈 나머지가 0일 때(짝수인 경우) 출력한다.
for num in numbers:
    if num == 237:
        break
    if num % 2 == 0:
        print(num)

# Console Output
# ---------------------------------------------
# 386
# 462
# 418
# 344
# 236
# 566
# 978
# 328
# 162
# 758
# 918



# 4. "google.com" string에서 각 character의 숫자를 dictionary로 변환하여 출력하도록
#     char_frequency 함수를 코딩하시오.

# input string
def char_frequency(str1):
    # coding here (pass 명령어를 제거하고 coding 할 것)
    # 딕셔너리를 만들고 처음 입력받는 값이라면 1로 설정, 그 이후는 += 1을 한다.
    char_dict = dict()

    for i in str1:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    
    return char_dict

print(char_frequency('google.com'))

# Console Output
# ---------------------------------------------
# {'o': 3, '.': 1, 'g': 2, 'l': 1, 'e': 1, 'c': 1, 'm': 1}



# 5. 다음 list에서 중복된 원소를 제거한 list를 생성후 출력하시오
# hint : my_list를 set data type으로 변환후 다시 list data type으로 변환

my_list = [10, 20, 30, 40, 20, 50, 60, 40]


#  coding here
# set()으로 중복 원소를 제거하고 list()로 다시 변환한다.
print(list(set(my_list)))

# Console Output
# ---------------------------------------------
# List of unique numbers :  [40, 10, 50, 20, 60, 30]



# 6. 다음 input dictionary 변수들을 합쳐서 새로운 dictionary로 만든 후 출력하시오

#  coding here
# update()를 통해 딕셔너리를 병합한다.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)

# Console Output
# ---------------------------------------------
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# 7. Input값을 숫자 n을 입력하면, key값을 1부터 n까지 하고, 각 key에 대한 value를 n*n으로
#    하는 dictionary를 만드시오.


#  coding here
# 딕셔너리를 만들어 입력한다.
num_dic = dict()

n = int(input("Input an integer : "))

for i in range(1, n+1):
    num_dic[i] = i*i

print(num_dic)
# Console Output
# ---------------------------------------------
# Input an integer : 10
# output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



# 8. 아래 tuple을 string으로 변환하여 출력하시오


#  coding here
# join()을 통해 빈 문자열을 튜플의 원소 사이사이에 삽입하여 문자열을 생성한다.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

print("".join(tup))

# Console Output
# ---------------------------------------------
# output : exercises



# 9. 아래 2개의 set setx, sety를 합친 set을 구하고 출력하시오


#  coding here
# 합집합을 통해 계산한다.
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])

setx |= sety

print(setx)

# Console Output
# ---------------------------------------------
# {'yellow', 'green', 'blue'}



# 10. 아래 List data type인 input_list의 각 원소인 tuple의 마지막 값을 기준으로
#     오름차순 정렬을 하는 sort_list_last함수를 완성후 이 함수를 호출하여 결과를 출력하시오

input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_list_last(tuples):
    # coding here (pass 명령어를 제거하고 coding 할 것)
    # lambda()함수를 통해 각 리스트 원소의 1번째 원소를 기준으로 정렬한다.
    return sorted(tuples, key=lambda x : x[1])

print(sort_list_last(input_list))


# Console Output
# ---------------------------------------------
# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]