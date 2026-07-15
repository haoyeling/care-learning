import random
answer = random.randint(1,100)
count = 0
while count < 7:
    guess_input = input("请输入一个1-100的数字: ")
    if not guess_input.isdigit():
        print("请输入有效数字！")
        continue
    num = int(guess_input)
    count += 1
    if num < answer:
        print(f"太小了!你还有{7 - count}次机会")
    elif num > answer:
        print(f"太大了！你还有{7 - count}次机会")
    else:
        print(f"恭喜你！猜对啦！你一共猜了{count}次！")
        break
    if count == 7 and answer != num:
        print(f"很遗憾，答案是{answer}")