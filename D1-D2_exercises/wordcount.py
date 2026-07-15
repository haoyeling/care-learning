"""词频统计：读文件、统计单词次数、输出最多的前10个。"""
# 读取文件全部内容
with open('sample.txt') as f:
    text = f.read()
words = text.split() #切成单词列表
counts = {} #空字典用来记录单词次数

# 遍历每个单词，累加它的个数
for word in words:
    counts[word] = counts.get(word, 0) + 1

# 按次数从高到低排序，sorted排序函数，reverse反转
top = sorted(counts.items(), key = lambda x : x[1], reverse=True)

# [:10]截取前十个;f"{word}"直接输出word变量值
for word,count in top[:10]:
    print(f"{word}: {count}")

# 另一种输出写法
# for pair in top[:3]:
    # print(pair)
