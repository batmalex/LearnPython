
mylist = ["Petya", "Vasya", "Egor", "Sasha", "Oleg", "Oleg", "Zghorick"]
print(mylist)
v = mylist.index("Egor")
print(v)

#mylist.append("Python")
#print(mylist)

#print(mylist[0], mylist[-1])

#print(len(mylist))
#del mylist[5:]
#print(len(mylist))

#for a in mylist:
 #   mylist.remove("Oleg")

#print(mylist)

#1
weather = {"city": "Москва", "temperature": "20", "wind": "восточный"}
#2
print(weather)
#3
weather["temperature"] = 30
print(weather)
#4
print(len(weather))
#5
print(weather.get("country"))
#6
weather["date"] = "27.05.2017"
print(weather)
#7
week_weather = []
dates = ["28.05.2017", "30.05.2017", "31.05.2017"]

for date in dates:
    weather = {"city": "Москва", "temperature": "20", "wind": "восточный"}
    weather["date"] = date
    print(weather)
    week_weather.append(weather)
    print(date)
print(week_weather)




