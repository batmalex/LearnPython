from flask import Flask, abort, request

from req import get_weather

from news_list import all_news


city_name = 'London'
api_key = '9fb3b0685690c2d66ef8be49d0fe3c81'


app = Flask(__name__)


@app.route("/")
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?APPID={0}&q={1}&units=metric'.format(api_key, city_name)
    weather = get_weather(url)
    result = '<meta http-equiv="refresh" content="30" ><br/>' + 'Температура {} \n'.format(weather['main']['temp'])
    result += '<br/>Город: {}'.format(weather['name'])
    return result


# @app.route("/news")
# def all_the_news():
#     for item in request.args:
#         print(item)
#         print(request.args.get(item))
#     return 'News'
@app.route("/news")
def all_the_news():
    limit = request.args.get('limit', 'all')
    color = request.args.get('color', 'black')
    return '<h1 style="color: {0}">News: <small>{1}</small></h1>'.format(color, limit)




@app.route("/news/<int:news_id>")
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    html_text = '<h1>{title}</h1><p><i>{date}</i></p><p>{text}</p>'.format(**news_to_show[0])
    # print(html_text)
    if len(news_to_show) == 1:
        return html_text
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5008)


