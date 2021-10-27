# Spacy identifies and recognizes pieces of text as different entities

import spacy

nlp = spacy.load('en_core_web_sm')

textfile = open('text for Spacy2.txt', 'r').read()

document = nlp(textfile)

for entity in document.ents:
    print(f"{entity.text}: {entity.label_}")

# spacy.explain() explains different abbreviations
print(spacy.explain('GPE')) # countries, cities, states
print(spacy.explain('LOC')) # Non-GPE locations, mountain ranges, bodies of water

from pathlib import Path

# function similar to Turnitin.com (analyzing for similarities in writings)
document1 = nlp(Path('RomeoAndJuliet.txt').read_text())
document2 = nlp(Path('EdwardTheSecond.txt').read_text())

# prints the percentage similarity of the two writings
print(document1.similarity(document2))