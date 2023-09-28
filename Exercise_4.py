Phrase = input("Напишите предложение на английском: ").lower()
Quantity = 0
for letter in Phrase:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        Quantity+=1
NewPhrase = Phrase.replace("ugly", "beauty")
print(f"Длина предложения = {len(Phrase)} символов. \nКоличество искомых гласных = {Quantity}. \nНовая фраза = {NewPhrase}."
      f"\n Начинается ли предложение с The - {NewPhrase.startswith('The')}. \nЗаканчивается ли на end - {NewPhrase.endswith('end')}")
