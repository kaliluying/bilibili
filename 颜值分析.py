# encoding:utf8
import base64
import json
import requests
from lxml import etree
import os


class BaiduAI:
    def __init__(self, img):
        self.AK = "gPhDSgW5atIAfFrqDqCv88xh"  # API Key
        self.SK = "wdDYfw3gYpNlbrbe1YOFR5oxeX8UOf52"  # SecretKey
        self.img_src = img
        self.headers = {
            "Content-Type": "application/json; charset=UTF-8"}

    def get_AccessToken(self):
        # 获取Access Token
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
        response = requests.get(host, headers=self.headers)
        json_result = json.loads(response.text)
        if response:
            return json_result['access_token']
        else:
            print(json_result)
            return 0

    def img_to_base64(slef, path):
        # 图片转化为base64
        with open(path, 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        return image_base64

    def face_identification(self, name):
        # 人脸检测与属性分析
        img = self.img_to_base64(self.img_src)
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        post_data = {
            "image": img,
            "image_type": "BASE64",
            "face_field": "beauty,gender",
            # 包括age,beauty,expression,face_shape,gender,glasses,landmark,emotion,face_type,mask,spoofing信息
            "face_type": "LIVE"  # 人脸的类型。LIVE表示生活照，IDCARD表示身份证芯片照，WATERMARK表示带水印证件照，CERT表示证件照片，默认LIVE。
        }
        access_token = self.get_AccessToken()
        request_url = request_url + "?access_token=" + access_token
        response = requests.post(url=request_url, data=post_data, headers=self.headers)
        json_result = json.loads(response.text)
        # print(json_result)
        if json_result['error_code'] == 0:
            print(name + '\t' + "人物性别：", json_result['result']['face_list'][0]['gender']['type'] + '\t' + "人物颜值评分：", json_result['result']['face_list'][0]['beauty'])
        else:
            print(json_result['error_code'])
            print(json_result['error_msg'])


class Beauty_img:
    def __init__(self):
        if not os.path.exists('./picture'):
            os.mkdir('./picture')
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        self.url = 'https://www.huya.com/g/2168'

    def page(self):
        response = requests.get(self.url, self.headers)
        if response.status_code == 200:
            return response.text
        return None

    def analysis(self, html):
        tree = etree.HTML(html)
        img_url_list = tree.xpath('//*[@id="js-live-list"]/li')
        for img_url in img_url_list:
            img = img_url.xpath('./a/img/@data-original')[0].split('?')[0]
            name = img_url.xpath('./a[2]/text()')[0]
            url = requests.get(img, self.headers).content
            img_path = 'picture/' + name + '.jpg'
            with open(img_path, 'wb')as f:
                f.write(url)
                print(name, '下载成功')

    def run(self):
        html = self.page()
        self.analysis(html)


if __name__ == '__main__':
    b = Beauty_img()
    b.run()
    root_path = 'picture'
    imglist = os.listdir(root_path)
    for i in range(0, len(imglist)):
        print('第{}张图片：'.format(i + 1), imglist[i])
        path = os.path.join(root_path, imglist[i])
        demo = BaiduAI(path)
        if demo.get_AccessToken():
            demo.face_identification(imglist[i])
