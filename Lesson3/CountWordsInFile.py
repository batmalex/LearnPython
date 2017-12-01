words_count = 0
symbols = set('~!@#$%^&*()_+=-";:,<>«»')
with open('./referat.txt', 'r') as f:
    for row in f:
        words_count += len(set(row.split()) - symbols)
print('В тексте {0} слов'.format(words_count))