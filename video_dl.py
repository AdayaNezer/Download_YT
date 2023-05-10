import argparse
from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"


def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
    except:
        print("Failed to download video")

    print("video was downloaded successfully")


def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")
