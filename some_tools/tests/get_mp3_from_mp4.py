# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:36
# @Author  : ihyf
# @File    : get_mp3_in_mp4.py
# @Software: PyCharm
# @ Desc :
import os


def get_mp3_from_mp4(ffmpeg_path, mp4_files_path):
    cmd = "ffmpeg.exe -i x.mp4 -vn -c:a copy out.mp3"

    for root, dirs, files in os.walk(mp4_files_path):
        for name in files:
            if name.endswith("mp4"):
                mp4_path = os.path.join(root, name)
                prefix = name[:name.rfind(".")]
                cmd = f"{ffmpeg_path} -i {mp4_path} -vn -c:a copy {prefix}.mp3"
                print(cmd)
                x = os.popen(cmd)
                f = x.read()
                print(f)


if __name__ == "__main__":
    ffmpeg_path = r"D:\app\ffmpeg_bin\ffmpeg.exe"
    mp4_files_path = r"D:\code\MyLeetCode\some_tools\mp4_files"
    get_mp3_from_mp4(ffmpeg_path, mp4_files_path)