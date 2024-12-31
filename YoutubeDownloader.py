from pytube import YouTube

def youtube_downloader():
    url = input("Enter the YouTube video URL: ")
    yt = YouTube(url)
    print(f"Downloading: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!") 

youtube_downloader()