from flask import Flask, abort, request

import json

app = Flask(__name__)

year_dict = {}
with open('./born_list.json', 'r') as f:
    name_data = json.loads(f.read())

    for row in name_data:
        name = row['Cells']['Name'].strip()
        number_of_persons = row['Cells']['NumberOfPersons']
        year = row['Cells']['Year']
        # print(year, name.rstrip(), number_of_persons)
        if year_dict.get(year, 0) == 0:
            year_dict[year] = {}
        year_dict[year][name] = year_dict[year].get(name, 0) + number_of_persons


def get_names(year):
    # for year in year_dict:
    name_list = [(name, number_of_persons) for name, number_of_persons in year_dict[year].items()]
    name_list = sorted(name_list, key=lambda count_names: count_names[1], reverse=True)
    return name_list


# n = get_names(2015)
# print(n)


@app.route("/names/<int:year_id>")
def names_in_year(year_id):
    body = str(get_names(year_id))
    # print(str(year_id))
    return body


if __name__ == "__main__":
    app.run(port=5005)

# @app.route("/news/<int:news_id>")
# def news_by_id(news_id):
#     news_to_show = [news for news in all_news if news['id'] == news_id]
#     html_text = '<h1>{title}</h1><p><i>{date}</i></p><p>{text}</p>'.format(**news_to_show[0])
#     # print(html_text)
#     if len(news_to_show) == 1:
#         return html_text
#     else:
#         abort(404)
#
#

