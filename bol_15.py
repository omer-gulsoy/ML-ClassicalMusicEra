import os
import librosa
import soundfile as sf

# .wav dosyalarının olduğu klasör
klasor_yolu = '/content/drive/MyDrive/ML_Projem/wav_dosyalarim'

# klasördeki tüm .wav dosyalarını listele
dosyalar = [f for f in os.listdir(klasor_yolu) if f.endswith('.wav')]

for dosya in dosyalar:
    tam_yol = os.path.join(klasor_yolu, dosya)

    # ses dosyasını oku
    y, sr = librosa.load(tam_yol, sr=None)  # sr=None: orijinal sample rate

    # toplam süre (saniye cinsinden)
    toplam_sure = len(y) / sr

    # kontrol: dosya en az 30 saniye mi?
    if toplam_sure >= 30:
        # 15 saniyelik örnek sayısı
        ornek_15s = int(sr * 15)

        ilk_15 = y[:ornek_15s]
        son_15 = y[ornek_15s:ornek_15s*2]

        # dosya adı parçasız
        isim, _ = os.path.splitext(dosya)

        # yeni dosyaları kaydet
        sf.write(os.path.join(klasor_yolu, f'{isim}_1.wav'), ilk_15, sr)
        sf.write(os.path.join(klasor_yolu, f'{isim}_2.wav'), son_15, sr)

        # eski dosyayı sil
        os.remove(tam_yol)

        print(f'{dosya} → {isim}_1.wav & {isim}_2.wav olarak bölündü ve silindi.')
    else:
        print(f'{dosya} → 30 saniyeden kısa, atlandı.')
