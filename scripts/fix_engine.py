
from pydub import AudioSegment, effects
import os

def auto_fix_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    fixed = effects.normalize(audio)
    fixed = fixed.fade_in(1000).fade_out(5000)
    fixed_path = "outputs/fixed/fixed_audio.wav"
    fixed.export(fixed_path, format="wav")
    return fixed_path
