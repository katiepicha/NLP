from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
import pandas as pd

# nltk.download("stopwords")

stops = stopwords.words("english")

# print(stops)

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

# list comprehension to remove stopwords
cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist)


# ROMEO AND JULIET

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

# word count
print(blob.words.count("joy"))
print(blob.word_counts["juliet"])
print(blob.words.count("thou"))

# noun phrases count
# print(blob.noun_phrases.count("lady capulet"))

# adding "thou", etc. to stopwords
more_stops = ["thee", "thou", "thy"]
stops += more_stops

# dictionary items - prints each word and number of times it appears in the text
items = blob.word_counts.items()
# print(items)

clean_items = [i for i in items if i[0] not in stops] 
print(clean_items[:10])

from operator import itemgetter

sorted_list = sorted(clean_items, key = itemgetter(1), reverse = True) # sorts it by number rather than alphabetical (default) and descending
print(sorted_list[:10])

# top 20 words in romeo and juliet

top20 = sorted_list[:20]

df = pd.DataFrame(top20, columns = ["word", "count"])
print(df)

# graph of top 20 words in romeo and juliet

import matplotlib.pyplot as plt

df.plot.bar(x = 'word', y = 'count', legend = False, color = ['y', 'c', 'm', 'b', 'g', 'r'])
plt.gcf().tight_layout()
plt.show()