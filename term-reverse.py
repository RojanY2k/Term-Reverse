text = "Quick Brown Fox jumps, The good drafting draw!"
max_word_length = len(max(text.split(), key=len))

text_args = [filter(None, (string + ",").split(" ")) for string in text.split(",")]
filled_args = [[text.ljust(max_word_length, " ") for text in t_a] for t_a in text_args]
inverted_texts = [
    [[word[index] + " " for word in data] for data in filled_args]
    for index in range(max_word_length)
][::-1]

new_text = ""
for i in range(len(text_args)):
    for index in range(len(inverted_texts)):
        new_text = new_text + "".join(map(str, inverted_texts[index][i])) + "\n"

print(new_text[:-1])
