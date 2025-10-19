print("введите текст:")
text = input()
reversed_splitted_text = ""
reversed_text = ""
word = ""

for char in text + " ":
    if char == " " and word != "":
        reversed_splitted_text = f"{word} {reversed_splitted_text} "
        word = ""
    elif char != " ":
        word = word + char

for i in range(len(text)-1, -1, - 1):
    reversed_text += text[i]

print("Инвертированные символы текста:", reversed_text)
print("Инвертированные слова текста:", reversed_splitted_text)