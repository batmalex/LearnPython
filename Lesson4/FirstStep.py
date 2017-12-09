from flask import Flask


from request import get_weather


city_name = 'Moscow'
api_key = '9fb3b0685690c2d66ef8be49d0fe3c81'


app = Flask(__name__)


@app.route("/")
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?APPID={0}&q={1}&units=metric'.format(api_key, city_name)
    weather = get_weather(url)
    result = 'Температура {}'.format(weather['main']['temp'])
    print(result)


if __name__ == "__main__":
    app.run()


