import string

print("введите текст:")
text = input()
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
secondary_text = ""
current_K = 0
K = 0

for char in text:  # отдельная логика обработки запрещенных символов
    if char in upper_case + lower_case + "., ":
        secondary_text += char

text = secondary_text
secondary_text = ""

for i in range(len(text)):
    if text[i] != " " and text[i] != ",": # логика обработки слов
        if current_K < 20:
            current_K += 1
            secondary_text += text[i]
    else: # выход из подсчета количества букв
        if current_K > K:
            K = current_K
        current_K = 0
        secondary_text += text[i]

text = secondary_text + "."
secondary_text = ""

for i in range(len(text)):
    if text[i] in lower_case:
        i_alphabet_index = [j for j in range(26) if lower_case[j] == text[i]][0] # номер буквы в алфавите
        secondary_text += lower_case[(i_alphabet_index + K) % 26]
    elif text[i] in upper_case:
        i_alphabet_index = [j for j in range(26) if upper_case[j] == text[i]][0]
        secondary_text += upper_case[(i_alphabet_index + K) % 26]
    else:
        secondary_text += text[i]

print("Зашифрованный текст:")
print(secondary_text)
