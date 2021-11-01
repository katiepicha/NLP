from textblob import TextBlob
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path
from wordcloud import WordCloud

stops = stopwords.words("english")
more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]
stops += more_stops

John = TextBlob(Path("book of John text.txt").read_text())
nouns = John.noun_phrases
items = John.word_counts.items()
clean_items = [i for i in items if i[0] not in stops and i[0] in nouns]

from operator import itemgetter
sorted_list = sorted(clean_items, key = itemgetter(1), reverse = True)
top15 = sorted_list[:15]
top15words = [i[0] for i in top15]
print(top15words)

noun_text = ' '.join(str(i) for i in top15words)

wordcloud = WordCloud(colormap = 'prism', background_color = 'white')
wordcloud = wordcloud.generate(noun_text)
wordcloud = wordcloud.to_file('Book of John Top15.png')