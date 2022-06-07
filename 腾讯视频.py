# 参考博客：https://www.cnblogs.com/yanweifeng/p/9501029.html
# http://vv.video.qq.com/getinfo?vids=b0136et5ztz&platform=101001&charge=0&otype=json
import requests
import json


class Ten:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }

    def page_Json(self):
        url_ = self.url.split('/')[-1].split('.')[0]
        url_json = f'http://vv.video.qq.com/getinfo?vids={url_}&platform=101001&charge=0&otype=json'
        response = requests.get(url_json, headers=self.headers)
        return json.loads(response.text.split('=')[1].replace(';', ''))

    def analysis(self, json_):
        name = json_['vl']['vi'][0]['ti']
        print(name)
        fvkey = json_['vl']['vi'][0]['fvkey']
        fn = json_['vl']['vi'][0]['fn']
        url = json_['vl']['vi'][0]['ul']['ui'][0]['url']
        video_url = url + fn + '?vkey=' + fvkey
        response = requests.get(video_url, headers=self.headers).content
        with open(f'{name}.mp4', 'wb') as f:
            f.write(response)

    def run(self):
        json_ = self.page_Json()
        self.analysis(json_)


url = 'https://v.qq.com/x/cover/mzc00200fm34tlu/h0042cty57h.html'
t = Ten(url)
t.run()
