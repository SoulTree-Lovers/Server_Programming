#!/usr/bin/env python3
#
# Client for the UINames.com service.

import requests


def SampleRecord():
    # https://dummyjson.com/을 실행하면 json data를 return함.
    r = requests.get("https://dummyjson.com/products", timeout=2.0)

    # requests.get 메소드에서 return된 r은 JSON format data인데,
    # json()메소드를 실행하면, dictionary data type으로 변환 (j는 dictionary data type)
    j = r.json()
    # 첫번째 station 객체 가져옴
    product = j['products'][0]

    return "Product title is {}\nDescription: {}\nprice: {}.".format(
        product["title"],
        product["description"],
        product["price"]
    )

if __name__ == '__main__':
    print(SampleRecord())
