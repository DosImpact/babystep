from __future__ import unicode_literals  # 왜쓰는지 모르겠어
import youtube_dl  # 가즈아
import os

workdir = os.path.dirname(os.path.realpath(__file__))  # 현재 작업중인 디렉터리 따오기.


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
    #

    # 1.1080p얻기 format인자로
    # bestvideo+bestaudio
    # 또는
    # bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio
    # 이거는 영상 음향 따로따로 나오는데...  그리고 병합해야된데..

    # 2. 그외 형식 best(최고화질/음질)/bestvideo(최고 영상만)/bestaudio(최고 음향만)
    #   코드 형식은  22 는 mp4인데 720p, 코드 18 - 360p mp4,
    'outtmpl':  workdir + '/' + 'Mark9',  # 임시제목
    'noplaylist': True,  # 플레이리스트
    'progress_hooks': [my_hook],  # 콜백함수? 다운로드 완료되면 status별로 print
    # ffmpeg 다운로드와 함께 파일 병합한다... 과정도 개빠름.
    'ffmpeg_location': 'C:\\ffmpeg\\bin\\',
    'playliststart': 1,  # 플레이 리스트라면 시작 인덱스~
    'playlistend': 10,

}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(
        'https://www.youtube.com/watch?v=RsHq6Q-7NsU&list=PLybyvF3WXLoy08qqUwvmAAurUUApvMV4K&index=1', download=True)
# 4K https://www.youtube.com/watch?v=IzS7ga4twH4
# 1080p https://www.youtube.com/watch?v=QYh6mYIJG2Y
# 5초 영상 테스트 https://www.youtube.com/watch?v=4A2rFdW_SVA

print('upload date : %s' % (meta['upload_date']))
print('uploader    : %s' % (meta['uploader']))
print('views       : %d' % (meta['view_count']))
print('likes       : %d' % (meta['like_count']))
print('dislikes    : %d' % (meta['dislike_count']))
print('id          : %s' % (meta['id']))
print('format      : %s' % (meta['format']))
print('duration    : %s' % (meta['duration']))
print('title       : %s' % (meta['title']))
print('description : %s' % (meta['description']))
