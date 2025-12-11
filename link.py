from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/playlist?list=PLZSHe_0xk6Mg0Oz8CYswTvHwZ0JrLG-KC"

ydl_opts = {
    'quiet': True,
    'extract_flat': True,  # Playlist içindeki linkleri almak için
    'skip_download': True,
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    urls = [entry['url'] if 'url' in entry else entry['webpage_url'] for entry in info['entries']]

# Linkleri yazdır
for url in urls:
    print(url)
