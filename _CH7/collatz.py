import math
#関数 collatz の定義
def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1

# ユーザーの入力を受け取り関数を実行する

try:
    input_number = int(input('正の整数を入力してください\n'))
    if input_number >= 1:
        while not input_number == 1:
            input_number = collatz(input_number)
            print(math.floor(input_number))
    else:
        raise ValueError
        
except ValueError:
    
    print('エラー!正の整数以外を入力しないでください')   
print('処理終了')
