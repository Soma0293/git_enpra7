import random

N = random.randint(100,999)

max = 5

for i in range(0,max):
    x = input ("3桁の数字を入力してください。")
    X = int(x)

    if X == N:
        print("正解です。")
    elif X > N:
        print("不正解です。もっと小さい数字です。")
    else:
        print("不正解です。もっと大きい数字です。")

print(f"正解は{N}です。")  



