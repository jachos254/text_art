from zalgo_text import zalgo


x = 'SUPREME_BEING'

y = zalgo.zalgo().zalgofy(x)

with open('zalgo.txt', 'w', encoding='utf-8') as f:
    f.write(y)