def word_count(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence:")
print(f"The number of words in the sentence is: {word_count(sentence)}")
