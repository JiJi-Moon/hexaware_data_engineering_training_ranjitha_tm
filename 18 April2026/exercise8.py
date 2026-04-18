sentence="python is easy and python is powerful"

sen_list=sentence.split(" ")

unique_words=list(set(sen_list))
print(unique_words)

word_count=dict()
for word in unique_words:
    word_count[word]=sen_list.count(word)
print(word_count)

