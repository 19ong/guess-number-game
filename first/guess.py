import random
num = random.randint(1,100)
print("猜数字游戏！数字范围1~100")
while True:
    guess = int(input("请输入你猜的数字："))
    if guess > num:
        print("大了！")
    elif guess < num:
        print("小了！")
    else:
        print("猜对啦！")
        break