# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 7:01
# @Author  : ihyf
# @File    : test1.py
# @Software: PyCharm
# @ Desc :
import os

"""
-loop 1 参数表示图片无限循环
-shortest参数表示音频文件结束，输出视频就结束。
相关链接
http://www.ruanyifeng.com/blog/2020/01/ffmpeg.html
https://www.zhihu.com/question/334876704/answer/750562451
"""

cmd_bak = "ffmpeg.exe -loop 1 -f image2 -framerate 1 -pix_fmt yuv420p -i xiaolei.jpg -i 2.mp3 -c:v libx264 -c:a copy -map 0:0 -map 1:a -s 1024x768  -shortest x.mp4"


def get_all_mp3(ffmpeg_path, mp3_files_path, jpg_path):
    # resolution 分辨率
    resolution = "1024x768"
    for root, dirs, files in os.walk(mp3_files_path):
        for name in files:
            if name.endswith("mp3"):
                mp3_path = os.path.join(root, name)
                prefix = name.split(".")[0]
                cmd = f"{ffmpeg_path} -loop 1 -f image2 -framerate 1 -pix_fmt yuv420p -i {jpg_path} -i {mp3_path} -c:v libx264 -c:a copy -map 0:0 -map 1:a -s {resolution}  -shortest {prefix}.mp4"
                print(cmd)
                x = os.popen(cmd)
                f = x.read()
                print(f)


if __name__ == '__main__':
    ffmpeg_path = r"D:\app\ffmpeg_bin\ffmpeg.exe"
    mp3_files_path = r"D:\code\MyLeetCode\some_tools\files"
    jpg_path = r"D:\code\MyLeetCode\some_tools\jpg\xiaolei.jpg"
    get_all_mp3(ffmpeg_path, mp3_files_path, jpg_path)