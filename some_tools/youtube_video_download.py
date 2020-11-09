# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 16:33
# @Author  : ihyf
# @File    : youtube_video_download.py
# @Software: PyCharm
# @ Desc :


from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
"""
only_audio=True ：只下载音频
only_video ：只下载视频
subtype='mp4' ：下载扩展名为“mp4”的文件，包括音频和视频
res="720p" ：下载清晰度为720p的视频
abr="64kbps" ：下载码率为64kbps的视频
video_codec="vp9" ：下载压缩格式为vp9的视频
audio_codec="vorbis" ：下载压缩格式为vorbis的音频
"""

url = "https://www.youtube.com/watch?v=NqC_1GuY3dw"
length = ""
output_path = "."
filename = ""
filename_prefix = ""

video = YouTube(url)
video.streams.filter(progressive=True, res="720p").all()
video.download(output_path, filename, filename_prefix)
