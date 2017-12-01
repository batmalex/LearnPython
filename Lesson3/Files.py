import csv
# cp1251
# with open("C:\\Projects\\text.txt", "a", encoding='utf-8') as f:
#     f.write("\t2Не получается!!,\n")
#
# with open("C:\\Projects\\text.txt", "r", encoding='utf-8') as f:
#     for line in f:
#         print("printing in one line.. {0}".format(line))
#
#     print(f.read())

# with open('C:\\Projects\\myfile.csv', 'r', encoding='cp1251') as f:
#     fields = ['first_name', 'last_name', 'mail', 'balance']
#     reader = csv.DictReader(f, fields, delimiter=';')
#     sum_bal = 0
#     for row in reader:
#         print(row)
#         sum_bal += float(row['balance'])
#     print(sum_bal)

# dict_list = [
#     {'first_name': 'pet', 'last_name': 'ывавыа', 'mail': 'asd', 'balance': '153'},
#     {'first_name': 'van', 'last_name': 'ivanov', 'mail': 'efrfl', 'balance': '215'}
#              ]
#
# dict_list =[{"привет": "И тебе привет!"}, {"как дела?": "нормуль"}, {"чем занят": "питон ботаю"}]
# with open('C:\\Projects\\myfile_2.csv', 'w', encoding='cp1251') as f:
#     fields = ['first_name', 'last_name', 'mail', 'balance']
#     writer = csv.DictWriter(f, fields, delimiter=';')
#     writer.writeheader()
#     for rows in dict_list:
#         writer.writerow(rows)
#
row =''
answers = {'question': "привет", 'answer': "И тебе привет!"}, {'question': "как дела?", 'answer': "нормуль"}, {'question': "чем занят", 'answer': "питон ботаю"}

with open('C:/Projects/myfile_2.csv', 'w', encoding='cp1251') as f:
    fields = ['question', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for row in answers:
        print(row)
        writer.writerow(row)