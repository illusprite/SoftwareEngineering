import re

with open("proba.txt", "r") as file:
    content = file.read().replace('\n', ' ')
    text = re.sub(r'[^\w\s]', '', content).split(" ")

print(f"Количество слов в статье: {len(text)}\n"
      f"Самое распространённое слово: {max(set(text), key=text.count)}. "
      f"Встречается {text.count('и')} раз")
