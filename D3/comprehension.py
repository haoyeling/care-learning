nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ['hello', 'hi', 'python', 'ok']
ping = [n * n for n in nums]
doubled = [n for n in nums if n % 2 == 0]
result = [n * n for n in nums if n > 5]
word = [n.upper() for n in words if len(n) >= 3]
print(f"{ping}")
print(f"{doubled}")
print(f"{result}")
print(f"{word}")