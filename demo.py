import re
from timeit import repeat
from tkinter import W, font
from turtle import back
import requests
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def page(url, headers=None):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def analysis(comment_html):
    comment = re.findall(r'<d p=".*?">(.*?)</d>', comment_html)
    temp = []
    for i in comment:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 1,2,3,4,5,6,7,8,9,]:
            temp.append(i)
    return ' '.join(temp)


def words(commet):
    mask = np.array(Image.open('ChinaMap.png'))
    wc = WordCloud(background_color='white', repeat=True, mask=mask, font_path='千图纤墨体.ttf')
    wc.generate(comment)
    wc.to_file('图云.png')


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV12t4y1n7b6?spm_id_from=333.337.search-card.all.click&vd_source=655ba79c7a5400218ba336bf2746db0e'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    html = page(url, headers)
    cid = re.findall(r'"cid":(.*?),', html)[0]
    comment_url = f'https://comment.bilibili.com/{cid}.xml'
    comment_html = page(comment_url, headers)
    comment = analysis(comment_html)
    words(comment)