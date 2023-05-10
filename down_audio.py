from pathlib import Path
from io import BytesIO
import streamlit as st
from pytube import YouTube


@st.cache_data(show_spinner=False, persist=True)
def download_audio_to_buffer(url):
    buffer = BytesIO()
    youtube_video = YouTube(str(url))
    audio = youtube_video.streams.get_audio_only()
    default_filename = audio.default_filename
    audio.stream_to_buffer(buffer)
    return default_filename, buffer


def download_audio(url):
    if url != '':
        with st.spinner("Downloading Audio Stream from Youtube..."):
            default_filename, buffer = download_audio_to_buffer(url)
        st.subheader("Title")
        st.write(default_filename)
        title_vid = Path(default_filename).with_suffix(".mp3").name
        st.subheader("Listen to Audio")
        st.audio(buffer, format='audio/mpeg')
        st.subheader("Download Audio File")
        with st.spinner('Downloading...'):
            button = st.download_button(
                label="Download mp3",
                data=buffer,
                file_name=title_vid,
                mime="audio/mpeg")
            if button:
                st.success('Download Complete', icon="✅")
                st.balloons()
