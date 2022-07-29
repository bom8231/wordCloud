from eunjeon import Mecab
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

with open('competition_title.txt', 'r', encoding='utf-8') as f:
    text = f.read()
tagger = Mecab()

nouns = tagger.nouns(text) #명사만 추출
words = [n for n in nouns if len(n) > 1] #길이가 1인 명사만 추출
while '공모전' in words:
    words.remove('공모전')

while '대회' in words:
    words.remove('대회')

while '경진' in words:
    words.remove('경진')

c = Counter(words)


img = Image.open('light.png')
img_array = np.array(img)

wc = WordCloud(font_path='C:/Windows/Fonts/nanumgothicextrabold.ttf', width=400, height=400, scale=2.0, max_font_size=250, mask=img_array)
gen = wc.generate_from_frequencies(c)

plt.figure()
plt.imshow(gen)
plt.show()

