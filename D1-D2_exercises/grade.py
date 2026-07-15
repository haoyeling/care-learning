import json
with open ('scores.txt') as f:
    scores = json.load(f)

for ch, word in scores.items():
    if word >= 90:
        print(f"{ch}: {word} 优秀")
    elif 90 > word >= 80:
        print(f"{ch}: {word} 良好")
    elif 80 > word >= 60:
        print(f"{ch}: {word} 及格")
    else:
        print(f"{ch}: {word} 不及格")