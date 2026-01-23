# 🎵 ML-ClassicalMusicEra: Classical Music Era Classification

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![HuggingFace](https://img.shields.io/badge/Transformers-Audio-yellow) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

This project presents a Transformer-based deep learning model capable of processing raw audio signals to classify classical music compositions into four distinct eras: **Baroque, Classical, Romantic, and Modern**.

Instead of traditional feature extraction methods, the project utilizes state-of-the-art "Pre-trained" audio models such as **Wav2Vec2, HuBERT, and WavLM** to predict the musical era directly from sound waves.

## 🎯 Project Goal

With the exponential growth of online multimedia content, automated classification of large-scale audio data has become crucial. This study aims to detect the musical era of a piece by analyzing its sonic characteristics (rhythm, harmony, instrumentation) using data collected from YouTube.

## 🛠️ Models Used (Transformers)

Five different models were fine-tuned and tested using the Hugging Face library:

| Model | Description |
| :--- | :--- |
| **HuBERT Base** | (facebook/hubert-base-ls960) - Learns hidden representations for robust feature extraction. |
| **WavLM Base** | (microsoft/wavlm-base) - Developed by Microsoft, highly resistant to noisy environments. |
| **Wav2Vec2 Base** | (facebook/wav2vec2-base-960h) - Effective in extracting meaningful representations from speech/audio signals. |
| **Distil-Wav2Vec2** | (OthmaneJ/distil-wav2vec2) - A lighter and faster optimized version. |
| **Wav2Vec2-KS** | (superb/wav2vec2-base-superb-ks) - Optimized for Keyword Spotting tasks. |

## 📂 Dataset & Pre-processing

The dataset was constructed by scraping YouTube using the `pytube` library.

* **Source:** YouTube (Baroque, Classical, Romantic, Modern era playlists).
* **Size:** Total of **21,437** audio files. Approximately 5,000 balanced samples per era.
* **Format:** Mono channel `.wav` files resampled to **16 kHz**.
* **Segmentation:** Each piece was split into **15-second** chunks for labeling.

## 📊 Experimental Results

Model performance was evaluated using Accuracy, F1-Score, Precision, Recall, and ROC AUC metrics.

* Training was conducted on **Google Colab (T4 GPU)**.
* Confusion Matrices and Loss graphs were analyzed for each model.
* **HuBERT** and **WavLM** demonstrated superior performance in capturing the complex distinctions between musical eras.

## 🚀 Installation

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/omer-gulsoy/ML-ClassicalMusicEra.git](https://github.com/omer-gulsoy/ML-ClassicalMusicEra.git)
    cd ML-ClassicalMusicEra
    ```

2.  **Install dependencies:**
    ```bash
    pip install torch transformers librosa pytube moviepy torchaudio numpy pandas
    ```

3.  **Data Collection (Optional):**
    Run the `data_collection.py` script (if available) to scrape new data from YouTube.

## 👥 Team & Acknowledgements

* **Developer:** Ömer Hasan GÜLSOY (Kocaeli University, Information Systems Engineering)
* **Contributors:** Ecem Su YILMAZ, Halit Mert ARTUN
* **Advisor:** Assoc. Prof. Dr. Zeynep Hilal KİLİMCİ

Special thanks to the open-source community and the musicians whose work inspired this project.

---
*This project was developed for the 2024-2025 Introduction to Machine Learning Course.*
