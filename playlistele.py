from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/playlist?list=PLIKKpLS_O-p0yy1PNN82Wv27oWpbFn48t"

ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'force_generic_extractor': False,
}

with YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(playlist_url, download=False)

video_titles = []

if 'entries' in result:
    for entry in result['entries']:
        video_titles.append(entry.get('title'))

# TXT dosyasına yaz
with open("video_listesi.txt", "w", encoding="utf-8") as f:
    for title in video_titles:
        f.write(title + "\n")

print("Video başlıkları 'video_listesi.txt' dosyasına yazıldı.")
