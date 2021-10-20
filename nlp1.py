from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
'''
# uses default analyzer (native analyser)
blob = TextBlob(text)

# breaks our text into two separate objects for each sentence
print(blob.sentences)

# makes a list of all the words in the text
print(blob.words)

# returns a list of tuples, each containing a word and a string representing its part-of-speech tag
print(blob.tags)

# returns a wordlist - a list of word objects
print(blob.noun_phrases)

# returns a Sentiment object indicating whether the text is positive or negative and whether it’s objective or subjective
    # polarity = sentiment cale from -1 to 1
    # subjectivity = 0.0 (objective) to 1.0 (subjective)
print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))
# sentiment analysis of individual sentences
for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))


# NAIVE BAYES ANALYZER

from textblob.sentiments import NaiveBayesAnalyzer

# specifies a specific analyzer (Naive Bayes)
blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())

# returns overall sentiment, percent positive, and percent negative
print(blob.sentiment)

# same at the sentence level
for sentence in blob.sentences:
    print(sentence.sentiment)


# TRANSLATE

spanish = blob.translate(to = 'es')
print(spanish)

chinese = blob.translate(to = 'zh')
print(chinese)
# translates back to english
print(chinese.translate())

'''
# SINGULAR AND PLURAL WORDS

from textblob import Word

# plural
index = Word('index')
print(index.pluralize())

# singular
cacti = Word('cacti')
print(cacti.singularize())

# wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


# SPELL CHECK AND CORRECTION

word = Word('theyr')

# spell check returns options for correction and percentage confidence
print(word.spellcheck())
# if you do not specify correction, it will pick the option with the highest confidence
print(word.correct())


# NORMALIZATION

word1 = Word("studies")
word2 = Word("varieties")

# stem - takes the stem of the word (not always accurate)
print(word1.stem())
print(word2.stem())

#lemmatize - gives us the singular form of the words
print(word1.lemmatize())
print(word2.lemmatize())


# DEFINITION, SYNONYM, ANTONYM from WordNet

happy = Word("happy")

# definition - returns a list of definitions
print(happy.definitions)

# synonym - prints a set of synonyms
print(happy.synsets)
# how to get the words as text
for s in happy.synsets: 
    for l in s.lemmas():
        print(l.name())
# grab directly
synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

# antonym
antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)