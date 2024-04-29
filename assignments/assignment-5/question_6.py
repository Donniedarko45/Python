sen = input("Enter a sentence: ")
words_set = set(sen.split())
count = {}

for word in words_set:
    count[word] = sen.count(word)

for word in words_set:
    print("Word", word, "occurred", count[word], "times.")
