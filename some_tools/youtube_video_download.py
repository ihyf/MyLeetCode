# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 16:33
# @Author  : ihyf
# @File    : youtube_video_download.py
# @Software: PyCharm
# @ Desc :
import os


def download_mp4(urls, output_path):
    """
    需要下载you-get:
        pip install you-get -i https://pypi.douban.com/simple
    """
    for url in urls:
        cmd = f"you-get {url} -o {output_path}"
        x = os.popen(cmd)
        f = x.read()
        print(f)


if __name__ == "__name__":
    output_path = r""
    urls = ["https://youtu.be/9Mpmk-r6dqU", "https://youtu.be/9Mpmk-r6dqU"]
    download_mp4(output_path)
