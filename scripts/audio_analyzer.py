from pydub import AudioSegment
import pyloudnorm as pyln
import numpy as np

def analyze_audio(file_path):
    # Load audio file
    audio = AudioSegment.from_file(file_path)
    
    # Duration in seconds
    duration = len(audio) / 1000.0

    # Create loudness meter
    loudness_meter = pyln.Meter(audio.frame_rate)

    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())

    # Calculate LUFS loudness
    loudness = loudness_meter.integrated_loudness(samples)

    # Calculate peak value (normalize by 16-bit max)
    peak = max(samples) / float(2**15)

    return {
        "duration_sec": duration,
        "loudness_LUFS": round(loudness, 2),
        "peak": round(peak, 3)
    }
