sent=input("Enter a Sentence: ")
word=input("Enter the word you have to cheak: ")
if word in sent:
    print("{} is present in {}".format(word,sent))
else:
   print("{} is not present in {}".format(word,sent))
