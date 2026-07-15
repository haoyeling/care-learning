nums = [3, 7, 3, 2, 9, 7, 3, 1, 9, 2]
a = set (nums) #set可以去重，查找速度快
print(f"去重后：{a}")
print(f"一共有{len(a)}个不同的数字")
count = {}
for word in nums:
    count[word] = count.get(word,0) + 1
top = sorted(count.items(), key = lambda x : x[1], reverse = True)
print (f"出现最多的是{top[0][0]},出现了{top[0][1]}次")
