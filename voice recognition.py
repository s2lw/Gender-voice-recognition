import sys
import librosa
import numpy as np
import time

def get_dominant_frequency(wav_path):
    audio_data, sr = librosa.load(wav_path, sr=None)

    N = len(audio_data)
    spectrum = np.fft.fft(audio_data)  # Transformacja Fouriera
    magnitude = np.abs(spectrum[:N // 2])  # Połowa widma, częstotliwości dodatnie
    freq = np.fft.fftfreq(N, d=1/sr)[:N // 2]

    hps = magnitude.copy()  # Harmonic Product Spectrum
    z = [2, 3, 4]

    for i in z:
        x = magnitude[::i]
        hps[:len(x)] *= x

    min_freq, max_freq = 85, 300

    valid_indices = (freq >= min_freq) & (freq <= max_freq)
    max_index = np.argmax(hps[valid_indices])
    dominant_frequency = freq[valid_indices][max_index]

    return dominant_frequency

if __name__ == "__main__":
    # Start pomiaru czasu
    start_time = time.time()

    # Odczyt ścieżki pliku WAV
    wav_path = sys.argv[1]

    # Wyznacz dominującą częstotliwość
    dominant_frequency = get_dominant_frequency(wav_path)

    # Określenie płci na podstawie dominującej częstotliwości
    result = "M" if dominant_frequency < 175 else "K"
    print(result)

    # Koniec pomiaru czasu
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Czas wykonania programu: {elapsed_time:.4f} sekundy")
