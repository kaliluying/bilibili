import re
import time
import requests
import numpy as np
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud


def clean(comment_list):
    comment = []
    for i in comment_list:
        if i not in ['0','1','2','3','4','5','6','7','8','9',0,1,2,3,4,5,6,7,8,9]:
            comment.append(i)
    df = pd.DataFrame()
    df['弹幕'] = comment
    df.to_csv('comment.csv')
    return ' '.join(comment)

# def clean(comment_list):
#     for i in comment_list:
#         if i in ['0','1','2','3','4','5','6','7','8','9',0,1,2,3,4,5,6,7,8,9]:
#             comment_list.remove(i)
#     return ' '.join(comment_list)

def page(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf8'
    if response.status_code == 200:
        return response.text

def analysis(comment):
    comment_list = re.findall(r'<d p=.*?>(.*?)</d>', comment)
    
    start = time.time()
    comment_str = clean(comment_list)
    stop = time.time()
    run_time = stop - start
    print(run_time)
    # print(comment_str)
    # mask = np.array(Image.open('ChinaMap.png'))
    # wc = WordCloud(background_color=None, repeat=True, height=480, width=854,mask=mask, mode='RGBA')
    # wc.generate(comment_str)
    # plt.axis("off")
    # plt.imshow(wc, interpolation="bilinear")
    # plt.show()
    # wc.to_file('c.png')

if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV12t4y1n7b6?spm_id_from=333.337.search-card.all.click&vd_source=655ba79c7a5400218ba336bf2746db0e'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
    html = page(url, headers)
    cid = re.findall(r'"cid":(.*?),', html)[0]
    comment_url = f'https://comment.bilibili.com/{cid}.xml'
    comment = page(comment_url, headers)
    analysis(comment)


