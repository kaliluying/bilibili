import requests
import re
from lxml import etree
from moviepy.editor import *

# 视频爬取
class Page:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "cookie": "l=v; _uuid=E0F64635-762D-9C83-894E-9D1FDFC6482345005infoc; buvid3=9958D3D2-4542-434E-83C5-6C14B51148F9148831infoc; rpdid=|(kRulmYkRu~0J'uYkmkYRklJ; LIVE_BUVID=AUTO3416337821636478; video_page_version=v_old_home; CURRENT_BLACKGAP=0; blackside_state=0; fingerprint3=9346170b26f0a26f1b6d432f6e74530f; fingerprint_s=ef74ecf0a9634bb2b6746601c08affe1; buvid4=2EF8D67D-8777-234B-8B0A-411632992C8313677-022012514-2vQi149BRC4QOzLPfbQP/unSt2U52mx2OgenmrzWoD81n+MyTmHT2A%3D%3D; buvid_fp_plain=undefined; bp_t_offset_671157361=625157353507097335; i-wanna-go-back=-1; PVID=1; bp_video_offset_1277486900=625137437740436200; bp_t_offset_1277486900=625160213953247689; sid=biz09vi1; buvid_fp=9ed681d40bc53d47bc97b03eba343ef6; DedeUserID=671157361; DedeUserID__ckMd5=ba8273578e2f6b80; SESSDATA=19a986c5%2C1659947404%2Cc8323*21; bili_jct=dde4aa320f76ad404d77418dd218f699; b_ut=5; CURRENT_QUALITY=80; fingerprint=9ed681d40bc53d47bc97b03eba343ef6; bp_video_offset_671157361=625905661361239800; b_lsid=594781108_17EECFC9E7D; innersign=1; CURRENT_FNVAL=80",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }

    # 获取页面源码
    def get_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        return None

    # 解析源码获得视频名称、链接
    def analysis(self, html):
        tree = etree.HTML(html)
        # 视频名称
        name = tree.xpath('//*[@id="viewbox_report"]/h1/text()')[0]
        # 视频链接列表
        video_list = tree.xpath('//script[contains(text(), "window.__playinfo__")]/text()')[0]
        # 视频链接
        video = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', video_list)[0]
        audio = re.findall(r'"audio":\[{"id":30280,"baseUrl":"(.*?)"', video_list)[0]
        return video, audio, name

    # 对链接发起请求，并进行合并存储
    def save(self, link):
        headers = {
            'referer': self.url,
            "cookie": "l=v; _uuid=E0F64635-762D-9C83-894E-9D1FDFC6482345005infoc; buvid3=9958D3D2-4542-434E-83C5-6C14B51148F9148831infoc; rpdid=|(kRulmYkRu~0J'uYkmkYRklJ; LIVE_BUVID=AUTO3416337821636478; video_page_version=v_old_home; CURRENT_BLACKGAP=0; blackside_state=0; fingerprint3=9346170b26f0a26f1b6d432f6e74530f; fingerprint_s=ef74ecf0a9634bb2b6746601c08affe1; buvid4=2EF8D67D-8777-234B-8B0A-411632992C8313677-022012514-2vQi149BRC4QOzLPfbQP/unSt2U52mx2OgenmrzWoD81n+MyTmHT2A%3D%3D; buvid_fp_plain=undefined; bp_t_offset_671157361=625157353507097335; i-wanna-go-back=-1; PVID=1; bp_video_offset_1277486900=625137437740436200; bp_t_offset_1277486900=625160213953247689; sid=biz09vi1; buvid_fp=9ed681d40bc53d47bc97b03eba343ef6; DedeUserID=671157361; DedeUserID__ckMd5=ba8273578e2f6b80; SESSDATA=19a986c5%2C1659947404%2Cc8323*21; bili_jct=dde4aa320f76ad404d77418dd218f699; b_ut=5; CURRENT_QUALITY=80; fingerprint=9ed681d40bc53d47bc97b03eba343ef6; bp_video_offset_671157361=625905661361239800; b_lsid=594781108_17EECFC9E7D; innersign=1; CURRENT_FNVAL=80",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        print('对链接发起请求')
        video = requests.get(link[0], headers=headers).content
        audio = requests.get(link[1], headers=headers).content

        name = link[2] + '1'
        print('下载视频')

        with open(f'{name}.mp4', 'wb') as f:
            f.write(video)
        with open(f'{name}.mp3', 'wb') as f:
            f.write(audio)

        # 合并
        print('合并视频')
        ffmpeg_tools.ffmpeg_merge_video_audio(f'{name}.mp4', f'{name}.mp3', f'{link[2]}.mp4')
        print('*' * 50)
        print('下载成功')
        print()

        # 删除之前的文件
        os.remove(f'{name}.mp4')
        os.remove(f'{name}.mp3')

    def run(self):
        html = self.get_page()
        print('获取到源码')
        link = self.analysis(html)
        print('获取到链接')
        self.save(link)


# 番剧失效
# 番剧爬取
class Drama(Page):
    def analysis(self, html):
        tree = etree.HTML(html)
        # 视频名称
        name = tree.xpath('//title/text()')[0]
        # 视频链接列表
        video_list = tree.xpath('//script[contains(text(), "window.__playinfo__")]/text()')[0]
        video = re.findall(r'"video":\[.*?"backupUrl":\["(.*?)"', video_list)[0]
        audio = re.findall(r'"audio":\[.*?"backupUrl":\["(.*?)"', video_list)[0]
        return video, audio, name


url_list = [
    'https://www.bilibili.com/video/BV1dm4y1o7YC?spm_id_from=333.1007.top_right_bar_window_history.content.click',
    'https://www.bilibili.com/video/BV1NZ4y1Z79G?spm_id_from=333.1007.top_right_bar_window_history.content.click']
# https://www.bilibili.com/bangumi/play/ep467225?from_spmid=666.4.0.0
for i in range(len(url_list)):
    if 'video' in url_list[i]:
        try:
            d = Drama(url_list[i])
            d.run()
        except:
            p = Page(url_list[i])
            p.run()
    else:
        p = Page(url_list[i])
        p.run()
