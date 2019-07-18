# coding: utf-8
from random import randint
def Game():
    ans=randint(1,100)
    guess=-3
    
    while guess!=ans:
        guess=int(input('請輸入一個數字:'))
        if guess>ans:
            print('太大了，再少一些')
        elif guess<ans:
            print('太小了，再多一些')
        else:
            print('BINGO!太厲害了')
play=True

while play:
    Game()
    print('-----------')
    again=input('再玩一次?')
    if again=='no':
        play=False
