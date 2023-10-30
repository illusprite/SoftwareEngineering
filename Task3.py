import re
with open("file2.txt", "w") as file:
    file.write(f"Beautiful is better than ugly. \n"
      f"Explicit is better than implicit. \n"
      f"Simple is better than complex. \n"
      f"Complex is better than complicated.")

with open("file2.txt", "r") as file:
    lines = len(file.readlines())

with open("file2.txt", "r") as file:
    content1 = file.read().replace('\n', '')
    words = len(re.sub(r'[^\w\s]', '', content1).split(" "))

with open("file2.txt", "r") as file:
    content2 = file.read().replace('\n', '')
    content2 = content2.replace(' ', '')
    letters = re.sub(r'[^\w\s]', '', content2)
    letters = len(list(letters))

print(f"Input file contains:\n"
      f"{letters} letters\n"
      f"{words} words\n"
      f"{lines} lines")