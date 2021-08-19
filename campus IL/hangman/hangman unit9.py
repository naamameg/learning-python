def choose_word(file_path, index):
    words_list = 0
    dict_of_words = {}
    with open(file_path, 'r') as handler:
        word_to_choose_from = handler.read().split(" ")
    for word in word_to_choose_from:
        if word not in dict_of_words:
            dict_of_words[word] = 1
        else:
            dict_of_words[word] += 1
    for word in dict_of_words.keys():
        words_list += 1
    chosen_word = word_to_choose_from[(index-1) % len(word_to_choose_from)]
    return (words_list, chosen_word)
print(choose_word(r"C:\Users\yuval\PycharmProjects\words.txt", 5))