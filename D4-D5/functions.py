def add(a, b):
    return a + b
def is_even(n):
    return n % 2 == 0
def count_words(text):
    word = text.split()
    return len(word)
def get_top_words(text, n):
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    top = sorted(count.items(), key =  lambda x : x[1], reverse = True)
    return top[:n] #return 直接返回列表，一旦执行函数立刻结束

print(add(3, 5))                       # 8
print(is_even(4))                      # True
print(count_words("hello world"))      # 2
print(get_top_words("the cat the dog the", 2))   # [('the', 3), ...]