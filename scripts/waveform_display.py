
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

def plot_waveform(file_path):
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples())
    plt.figure(figsize=(10, 3))
    plt.plot(samples)
    plt.title("Waveform")
    st.pyplot(plt)
