from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("C:\ProgrammProjekte\Python\LearnPaython_Class\Python lernen\Teil_05_Alice_in_wonderland.txt", "r") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)

STOPWORDS.add('said')
STOPWORDS.add('Illustration')

wordcloud.generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
