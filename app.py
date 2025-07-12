
import streamlit as st
from scripts.audio_analyzer import analyze_audio
from scripts.fix_engine import auto_fix_audio
from scripts.qc_reporter import generate_reports
from scripts.waveform_display import plot_waveform

st.set_page_config(page_title="ZULFIYAAN MASTERING PRO", layout="wide")

st.title("🎧 ZULFIYAAN MASTERING PRO - Full QC & Auto Fix")

uploaded_file = st.file_uploader("Upload FLAC or WAV File", type=["flac", "wav"])

if uploaded_file:
    with open("input_audio.wav", "wb") as f:
        f.write(uploaded_file.read())
    st.audio("input_audio.wav")
    st.success("Audio uploaded. Starting analysis...")

    qc_results = analyze_audio("input_audio.wav")
    st.json(qc_results)

    st.info("🔧 Auto fixing...")
    fixed_path = auto_fix_audio("input_audio.wav")

    st.audio(fixed_path)
    st.success("✅ Audio fixed and ready for download.")

    plot_waveform(fixed_path)

    reports = generate_reports("input_audio.wav", fixed_path, qc_results)
    for rname, rfile in reports.items():
        with open(rfile, "rb") as f:
            st.download_button(f"⬇️ Download {rname}", f, file_name=rfile.split("/")[-1])
