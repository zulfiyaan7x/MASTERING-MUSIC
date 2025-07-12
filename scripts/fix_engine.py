from pydub import AudioSegment, effects
import os

def auto_fix_audio(file_path):
    # Load audio
    audio = AudioSegment.from_file(file_path)

    # ✔️ Apply audio mastering-style fixes (you can extend this logic)
    fixed = effects.normalize(audio)  # Normalize volume
    fixed = fixed.fade_in(500).fade_out(4000)  # Fade-in (0.5s), Fade-out (4s)

    # 📁 Define fixed output path
    output_dir = "output"
    fixed_filename = "fixed_audio.wav"
    fixed_path = os.path.join(output_dir, fixed_filename)

    # ✅ Ensure output folder exists
    os.makedirs(output_dir, exist_ok=True)

    # 💾 Export fixed audio as WAV
    fixed.export(fixed_path, format="wav")

    return fixed_path
