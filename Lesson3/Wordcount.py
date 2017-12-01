# word_count = input("Ведите строку")
word_count = 'привет "мишка на севере» конфетка такая есть кукуруза желтая"'
print(word_count.count('"'))
# print(word_count)
count = 0
string_start = 0
word_start = 0

for word in word_count:
    if word in ('"', '“') and string_start == 0:
        string_start = 1
    elif word in ('"', '”') and string_start == 1:
        string_start = 0
        word_start = 0
    else:
        if not word.isspace() and string_start == 1:
            if word_start == 0:
                word_start = 1
                count += 1
            elif word_start == 1:
                pass
        if word.isspace() and string_start == 1:
            if word_start == 1:
                word_start = 0
print(count)

