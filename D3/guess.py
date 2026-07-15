import random
answer = random.randint(1,100)
count = 0
while True:
    num = int(input("请输入一个1-100的数字: "))
    count += 1
    if num < answer:
        print("太小了")
    elif num > answer:
        print("太大了")
    else:
        break
print(f"恭喜你！猜对啦！你一共猜了{count}次！")
