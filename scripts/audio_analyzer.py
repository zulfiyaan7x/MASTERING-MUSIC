
from pydub import AudioSegment
import pyloudnorm as pyln

def analyze_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio) / 1000.0
    loudness_meter = pyln.Meter(audio.frame_rate)
    samples = audio.get_array_of_samples()
    loudness = loudness_meter.integrated_loudness(samples)
    peak = max(samples) / (2**15)
    return {
        "duration_sec": duration,
        "loudness_LUFS": round(loudness, 2),
        "peak": round(peak, 3)
    }
