import os
import matplotlib.pyplot as plt

# Klasör yolları
base_path = r"G:\Drive'ım\ML - Klasik Müzik Dönemi\muzikler"
folders = ["baroque", "classic", "modern", "romantic"]

counts = []

# Her klasördeki .wav dosyalarını say
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    count = sum(1 for root, _, files in os.walk(folder_path) for file in files if file.endswith('.wav'))
    counts.append(count)
    print(f"{folder}: {count} dosya")

# Çubuk grafik çizimi
plt.figure(figsize=(8, 5))
plt.bar(folders, counts, color=["#8B4513", "#4682B4", "#32CD32", "#DA70D6"])
plt.title("Müzik Dönemlerine Göre WAV Dosyası Sayısı")
plt.xlabel("Müzik Dönemi")
plt.ylabel("Dosya Sayısı")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
