import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
secondary_text = ""
indexes_of_dot = []
current_K = 0
text = ""
K = 0

print("введите текст:")

while "." not in text:
    print("ОН ДОЛЖЕН СОДЕРЖАТЬ ТОЧКУ!")
    text = input(text)

for i in range(len(text)):
    if text[i] == ".":
        indexes_of_dot.append(i)

for i in range(indexes_of_dot[0] + 1):  # отдельная логика обработки запрещенных символов
    if text[i] in upper_case + lower_case + "., ":
        secondary_text += text[i]

text = secondary_text
secondary_text = ""

for i in range(len(text)):
    if text[i] != " " and text[i] != ",": # логика обработки слов
        if current_K < 20:
            current_K += 1
            secondary_text += text[i]
        else:
            secondary_text += " "
            secondary_text += text[i]
            current_K = 0
    else: # выход из подсчета количества букв
        if current_K > K:
            K = current_K
        current_K = 0
        secondary_text += text[i]

text = secondary_text
secondary_text = ""

for i in range(len(text)):
    if text[i] in lower_case:
        i_alphabet_index = [] # номер буквы в алфавите
        for j in range(26):
            if lower_case[j] == text[i]:
                i_alphabet_index.append(j)
        secondary_text += lower_case[(i_alphabet_index[0] + K) % 26]

    elif text[i] in upper_case:
        i_alphabet_index = []
        for j in range(26):
            if upper_case[j] == text[i]:
                i_alphabet_index.append(j)
        secondary_text += upper_case[(i_alphabet_index[0] + K) % 26]

    else:
        secondary_text += text[i]

print("Зашифрованный текст:")
print(secondary_text)
