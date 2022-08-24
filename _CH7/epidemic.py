epidemic = 'ぎゅうぎゅうの口の感の狂った短気のデブがけつようぴに遊びにでんとアフリカのスーダンにこられペットにヒナを貰った'
# print(len(epidemic))
for i in range(len(epidemic)):
    aster1 = '*' * (i + 1)
    aster2 = '*' * (len(epidemic) - i)
    print(f'{str(i).zfill(2)} {aster1}{epidemic[i]}{aster2}')
