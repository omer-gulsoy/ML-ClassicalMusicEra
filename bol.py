import os
from pydub import AudioSegment

# Ana dizinler
input_root = "C:/Users/win11/Documents/Projeler/ML - klasik müzik dönemi/ham"  # Ham müzik dosyalarının bulunduğu klasör
output_root = "C:/Users/win11/Documents/Projeler/ML - klasik müzik dönemi/muzikler"  # Parçaların kaydedileceği klasör

# Her dönem için ilgili klasörler
periods = ["baroque", "classic", "romantic"]

# Parça süresi (30 saniye)
segment_duration = 30 * 1000  # 30 saniye (milisaniye cinsinden)

# Her dönem için işlem yapalım
for period in periods:
    period_folder = os.path.join(input_root, period)  # Örneğin: "ham/baroque"
    output_period_folder = os.path.join(output_root, period)  # Örneğin: "muzikler/baroque"
    
    # Eğer çıkış klasörü yoksa oluştur
    if not os.path.exists(output_period_folder):
        os.makedirs(output_period_folder)
    
    # Her dosyayı tek tek işle
    for file_name in os.listdir(period_folder):
        if file_name.endswith(".wav"):  # Yalnızca .wav dosyalarını al
            file_path = os.path.join(period_folder, file_name)
            
            # Müzik dosyasını yükle
            audio = AudioSegment.from_wav(file_path)
            
            # Parçalama işlemi
            duration = len(audio)
            part_count = duration // segment_duration  # Kaç parça olduğunu hesapla
            
            # Dosya adı ve hedef klasörü oluştur
            song_name = os.path.splitext(file_name)[0]
            output_song_folder = os.path.join(output_period_folder, song_name)
            
            # Parçaların kaydedileceği klasörü oluştur
            if not os.path.exists(output_song_folder):
                os.makedirs(output_song_folder)
            
            # 30 saniyelik parçalara böl
            for i in range(part_count):
                start_time = i * segment_duration
                end_time = start_time + segment_duration
                segment = audio[start_time:end_time]
                
                # Parçayı kaydet
                segment_name = f"part{i+1}.wav"
                segment_path = os.path.join(output_song_folder, segment_name)
                segment.export(segment_path, format="wav")
            
            # Orijinal dosyayı sil
            os.remove(file_path)
            print(f"{file_name} başarıyla parçalandı ve silindi.")
