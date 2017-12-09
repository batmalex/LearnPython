import requests


def get_weather(url):
    result = requests.get(url)
    # print(type(result.text))
    # print(result.json())
    if result.status_code == 200:
        return result.json()
    else:
        print("WTF!")


# if __name__ == "__main__":
#     r = get_weather('http://api.openweathermap.org/data/2.5/weather?APPID=9fb3b0685690c2d66ef8be49d0fe3c81&q=Moscow&units=metric')
#     print(r)


# 9fb3b0685690c2d66ef8be49d0fe3c81