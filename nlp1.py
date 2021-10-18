from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

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