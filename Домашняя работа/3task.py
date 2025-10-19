import string

print("введите text")
text = input() + " "
words_counts = []
words = []
read_word = ""

for char in text:
    if char == " " and read_word != "":
        words.append(read_word)
        read_word = ""
    elif char != " ":
        if char in string.ascii_uppercase:
            char_alphabet_index = []
            for j in range(26):
                if string.ascii_uppercase[j] == char:
                    char_alphabet_index.append(j)
            read_word += string.ascii_lowercase[char_alphabet_index[0]]
        else:
            read_word = read_word + char

for counting_word in set(words):
    count = 0
    for word in words:
        if counting_word == word:
            count += 1
    words_counts.append((counting_word, count))

for upper_border in range(len(words_counts), 0, -1):
    for i in range(upper_border - 1):
        if words_counts[i][1] < words_counts[i + 1][1]:
            words_counts[i], words_counts[i + 1] = words_counts[i + 1], words_counts[i]

print("топ 5 самых используемых слов:")

for i in range(min(len(words_counts), 5)):
    print(words_counts[i][0], words_counts[i][1])