def read_text(filename):
    """读取文件,返回小写后的文本"""
    with open(filename) as f:
        text = f.read().lower()
    return text

def count_chars(text):
    """返回字符数"""
    return len(text)

def count_words(text):
    """返回单词数"""
    words = text.split()
    return len(words)

def count_lines(text):
    """返回行数"""
    lines = text.split('\n')
    return len(lines)

def average_word_length(text):
    """返回平均词长"""
    words = text.split()
    total = 0
    for word in words:
        word = word.strip('.')
        total = total + len(word)
    return total / len(words)

def get_top_words(text, n=3):
    """返回出现最多的 n 个词"""
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    top = sorted(count.items(), key = lambda x : x[1], reverse = True)
    return top[:n]

def print_report(filename, n = 3):
    """打印完整报告(调用上面所有函数)"""
    text = read_text(filename)
    print("===== 文本分析报告 =====")
    print(f"总字符数: {count_chars(text)}")
    print(f"总单词数: {count_words(text)}")
    print(f"总行数: {count_lines(text)}")
    print(f"平均词长: {average_word_length(text):.1f}")
    print(f"出现最多的{n}个词: {get_top_words(text, n)}")

print_report('report.txt', 5)


