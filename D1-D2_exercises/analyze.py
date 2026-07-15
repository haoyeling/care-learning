with open('report.txt') as f:
    text = f.read().lower()
print(f"===== 文本分析报告 =====")
print(f"总字符数(含空格标点)：{len(text)}")
words = text.split()
print(f"总单词数：{len(words)}")
lines = text.split('\n')
print(f"总行数：{len(lines)}")
count = {}
total = 0
for word in words:
    word = word.strip('.')
    total = total + len(word)
    count[word] = count.get(word, 0) + 1
top = sorted(count.items(), key = lambda x: x[1], reverse = True)
average = total/len(words)
print(f"平均词长: {average:.1f}")
print(f"高频词 Top3:")
for word,num in top[:3]:
    print(f"  {word}: {num}")
