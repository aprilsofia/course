<<<<<<< HEAD
# coding: utf-8
words=['',
 '我',
 '我的',
 '妳',
 '妳的',
 '心',
 '溫柔',
 '日子',
 '雨',
 '風',
 '天空',
 '雲',
 '等待',
 '哭泣',
 '戀愛',
 '相遇',
 '分離',
 '忘記',
 '心醉',
 '驀然',
 '吹過',
 '思念',
 '靈魂',
 '停止',
 '喜悅',
 '分享',
 '旅行',
 '']
from random import choices,randint,sample
n=randint(5,14)

for i in range(n):
    m=randint(3,6)
    sentence=sample(words,m)
    print(" ".join(sentence))
def poem():
    n=randint(5,14)

    for i in range(n):
        m=randint(3,6)
        sentence=sample(words,m)
        print(" ".join(sentence))
poem()
=======
# coding: utf-8
words=['',
 '我',
 '我的',
 '妳',
 '妳的',
 '心',
 '溫柔',
 '日子',
 '雨',
 '風',
 '天空',
 '雲',
 '等待',
 '哭泣',
 '戀愛',
 '相遇',
 '分離',
 '忘記',
 '心醉',
 '驀然',
 '吹過',
 '思念',
 '靈魂',
 '停止',
 '喜悅',
 '分享',
 '旅行',
 '']
from random import choices,randint,sample
n=randint(5,14)

for i in range(n):
    m=randint(3,6)
    sentence=sample(words,m)
    print(" ".join(sentence))
def poem():
    n=randint(5,14)

    for i in range(n):
        m=randint(3,6)
        sentence=sample(words,m)
        print(" ".join(sentence))
poem()
>>>>>>> 73c276544eb715f0ce98fab080cd6dfc1fda8845
