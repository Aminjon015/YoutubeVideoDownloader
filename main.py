from pytube import YouTube
import ffmpeg

URL = input('Enter link of Video: ')

DOWNLOAD_DIRECTORY = 'Downloads'


def download_video(url):
    yt = YouTube(url)
    # yt.streams.get_highest_resolution().download(DOWNLOAD_DIRECTORY)
    stream_video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    stream_video.download(DOWNLOAD_DIRECTORY, 'video')
    if not stream_video.is_progressive:
        stream_audio = yt.streams.get_audio_only()
        stream_audio.download(DOWNLOAD_DIRECTORY, 'audio')
        combine(DOWNLOAD_DIRECTORY + '/audio', DOWNLOAD_DIRECTORY + '/video')
        print(stream_audio)
    print(stream_video)

def combine(audio, video):
    video_stream = ffmpeg.input(audio)
    audio_stream = ffmpeg.input(video)
    ffmpeg.output(audio_stream, video_stream, DOWNLOAD_DIRECTORY + '/result.mp4').run()


if __name__ == '__main__':
    download_video(URL)

