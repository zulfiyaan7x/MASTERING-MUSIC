import numpy as np
import pyloudnorm as pyln
from pydub import AudioSegment
import os

def analyze_audio(file_path):
    # Load audio file using pydub
    audio = AudioSegment.from_file(file_path)

    # Extract raw samples and convert to float
    samples = np.array(audio.get_array_of_samples())
    
    # If stereo, reshape to 2D and average channels
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
        samples = samples.mean(axis=1)

    # Convert to float32 in range [-1.0, 1.0]
    samples = samples.astype(np.float32) / (2 ** 15)

    # Sampling rate
    sample_rate = audio.frame_rate

    # Duration
    duration_sec = len(audio) / 1000.0

    # Create loudness meter
    meter = pyln.Meter(sample_rate)

    # Integrated loudness
    loudness = meter.integrated_loudness(samples)

    # True peak (approx)
    peak = np.max(np.abs(samples))

    return {
        "duration_sec": round(duration_sec, 2),
        "sample_rate": sample_rate,
        "bit_depth": audio.sample_width * 8,
        "channels": audio.channels,
        "loudness_LUFS": round(loudness, 2),
        "true_peak": round(peak, 3)
    }
