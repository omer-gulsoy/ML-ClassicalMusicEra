
🎼 Klasik Müzik Dönemi Sınıflandırması Veri Toplama

Bu proje, klasik müzik eserlerini Barok, Klasik, Romantik ve Modern dönemlerine ayırarak veri seti oluşturmayı amaçlar. Spotify çalma listelerinden ses dosyaları indirip 30 saniyelik parçalara bölünür. Makine öğrenmesi projesinde kullanılmak üzere yapılandırılmıştır.

📁 Klasör Yapısı

ML - klasik müzik dönemi/
│
├── indir.py       # Spotify'dan ses dosyalarını indirir ve böler
├── bol.py         # Daha önce indirilen ama bölünememiş ses dosyalarını 30s parçalara ayırır
│
├── ham/           # Spotify'dan indirilen orijinal .wav dosyaları
│   ├── baroque/
│   ├── classic/
│   ├── romantic/
│   └── modern/
│
└── muzikler/      # 30 saniyelik segmentlere ayrılmış dosyalar
    ├── baroque/
    │   └── Parça Adı/
    │       ├── part1.wav
    │       ├── part2.wav
    │       └── ...
    ├── classic/
    ├── romantic/
    └── modern/

⚙️ Gereksinimler

- Python 3.10+
- ffmpeg (sisteme kurulu ve PATH'e eklenmiş olmalı)

Python Paketleri

pip install -r requirements.txt

Eğer requirements.txt dosyası yoksa, aşağıdaki paketleri tek tek yükleyebilirsin:

pip install yt-dlp
pip install pydub

🔧 Kullanım

1. Müzik İndirme ve Parçalama

python indir.py

Bu script:
- linkler.txt içindeki çalma listelerini okur.
- ham/ klasörüne müzikleri indirir.
- Her müziği 30 saniyelik parçalara böler.
- Sonuçları muzikler/ klasörüne kaydeder.
- Alan tasarrufu için orijinal dosyayı siler.

2. Bölünmemiş Dosyaları Parçalama

python bol.py

Bu script:
- ham/ klasöründe zaten indirilen dosyaları kontrol eder.
- Parçalanmamış olanları 30 saniyelik bölümlere ayırır.
- muzikler/ klasörüne yerleştirir.
- İşlem bitince orijinali siler.

📌 Notlar

- Her döneme ait müzikler ayrı klasörlerde organize edilmelidir.
- Dosya adlarında Türkçe karakter ve boşluklar yerine - veya _ kullanılması önerilir.
- Yeterli disk alanı gereklidir; indir.py ve bol.py, işlemlerden sonra ham dosyaları silerek yer kazandırır.

👨‍💻 Hazırlayan

Bu proje bir makine öğrenmesi dersi kapsamında klasik müzik dönemini ses verisinden tahmin etmeye yönelik veri hazırlama adımıdır.
