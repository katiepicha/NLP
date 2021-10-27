from pathlib import Path
import imageio
from wordcloud import WordCloud

# bring in the text
text = Path('RomeoAndJuliet.txt').read_text()

# bring in the heart mask
mask_image = imageio.imread('mask_heart.png')

# create a wordcloud with the specified color/images/etc.
wordcloud = WordCloud(colormap = 'prism', mask = mask_image, background_color = 'white')

# feed wordcloud the text
wordcloud = wordcloud.generate(text)

# send generated wordcloud to a file
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

print('done')
