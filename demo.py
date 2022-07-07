import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

mask = np.array(Image.open('ChinaMap.png'))

df = pd.DataFrame()
text = "hello world world python javascript c c++ python"


wc = WordCloud(background_color=None, repeat=True, height=480, width=854,mask=mask, mode='RGBA')
wc.generate(text)

# plt.axis("off")
# plt.imshow(wc, interpolation="bilinear")
# plt.show()
wc.to_file('c.png')