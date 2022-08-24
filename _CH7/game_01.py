#数当てゲーム
import random
secret_number = random.randint(1, 20)
print('1~20の数字を当ててください\n')

#6回聞く
for guess_taken in range(1, 7):
    print('数を入力してください')
    guess = int(input())

    if guess < secret_number:
        print('小さいです｡')
    elif guess > secret_number:
        print('大きいです｡')
    else:
        break # 当たり!

if guess == secret_number:
    print('当たり!"' + str(guess_taken) + '"回で当たりました｡')
else:
    # print('残念｡正解は ' + str(secret_number) + 'でした｡')
    print(f'残念｡正解は"{secret_number}"でした')
