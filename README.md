# Gender Classification Based on Voice Frequency

## Description
This script analyzes the dominant frequency of a WAV file to classify the speaker's gender. It uses the Fourier Transform and Harmonic Product Spectrum (HPS) to determine the main frequency component of the audio signal. Based on this frequency, the program assigns "M" for male voices (below 175 Hz) and "K" for female voices (175 Hz and above).

## Accuracy
- Training set accuracy: 93%
- Test set accuracy: 84%

## Requirements
- Python 3
- Required libraries:
  - librosa
  - numpy

The program will output:
- "M" for male voices
- "K" for female voices
- Execution time in seconds

## How It Works
1. Loads the WAV file and extracts audio data.
2. Computes the frequency spectrum using the Fast Fourier Transform (FFT).
3. Applies the Harmonic Product Spectrum (HPS) to enhance dominant frequencies.
4. Identifies the strongest frequency within the human voice range (85 Hz - 300 Hz).
5. Classifies the speaker based on the detected frequency.


