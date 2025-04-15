def word_count_with_frequency(sentence):
    words = sentence.split()
    word_count = len(words)
    word_frequency = {}

    for word in words:
        word = word.lower()
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_count, word_frequency

sentence = input("Enter a sentence: ")
count, frequency = word_count_with_frequency(sentence)
print(f"The number of words in the sentence is: {count}")
print("Word frequencies:", frequency)


