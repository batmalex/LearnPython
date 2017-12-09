import requests
import json


def get_weather(url):
    result = requests.get(url).json()
    with open('./born_list.json', 'w') as f:
        file_to_output = json.dumps(result, ensure_ascii=False)
        f.write(file_to_output)


if __name__ == "__main__":
     r = get_weather('http://apidata.mos.ru/v1/datasets/2009/rows?api_key=f1258a3531b18877b70f2cf57abfa05d')
     print(r)

# f1258a3531b18877b70f2cf57abfa05d