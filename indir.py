import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
from pathlib import Path

# Ayarlar
input_folder = "playlistler"
output_root = "muzikler"
segment_duration = 30 * 1000  # 30 saniye

# YouTube indirici ayarları
ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

# Tüm txt dosyalarını tara
for txt_file in os.listdir(input_folder):
    if txt_file.endswith(".txt"):
        period_name = txt_file.replace(".txt", "").lower()
        txt_path = os.path.join(input_folder, txt_file)

        with open(txt_path, "r", encoding="utf-8") as file:
            urls = file.read().splitlines()

        for idx, url in enumerate(urls):
            print(f"[{period_name.upper()}] ({idx+1}/{len(urls)}): {url}")
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
                    title = Path(filename).stem

                    # Hedef klasör: baroque/A eser adı/
                    target_folder = os.path.join(output_root, period_name, f"{title}")
                    os.makedirs(target_folder, exist_ok=True)

                    # Ses dosyasını parçala
                    audio = AudioSegment.from_wav(filename)
                    duration = len(audio)
                    for i in range(0, duration, segment_duration):
                        segment = audio[i:i + segment_duration]
                        segment_path = os.path.join(target_folder, f"part{i // segment_duration + 1}.wav")
                        segment.export(segment_path, format="wav")

                    os.remove(filename)  # Ana dosyayı sil

            except Exception as e:
                print(f"Hata oluştu: {e}")
