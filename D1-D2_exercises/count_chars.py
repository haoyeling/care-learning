text = "hello world"
count = {}
for word in text:
    if word == ' ':
        continue
    count[word] = count.get(word,0) + 1
for ch,word in count.items():
    print(f"{ch}: {word}")