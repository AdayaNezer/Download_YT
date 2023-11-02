from pytube import YouTube
import streamlit as st
from io import BytesIO
from pathlib import Path

@st.cache_data(show_spinner=False, persist=True)
def download_video_to_buffer(url):
    try:
        buffer = BytesIO()
        youtube_video = YouTube(str(url))
        video = youtube_video.streams.get_highest_resolution()
        default_filename = video.default_filename
        video.stream_to_buffer(buffer)
        return default_filename, buffer
    except:
        st.error(
            "👉 Please only insert a YouTube link", icon="😡")
        return -1, -1

def download_video(url):
    if url != '':
        with st.spinner("Downloading video Stream from Youtube..."):
            default_filename, buffer = download_video_to_buffer(url)
            if default_filename == -1 and buffer == -1:
                st.error("❌💥💥💥💥💥💥❌")
                return
        st.subheader("Title")
        st.write(default_filename)
        title_vid = Path(default_filename).with_suffix(".mp4").name
        st.subheader("watch the video")
        st.video(buffer, format='video/mpeg')
        st.subheader("Download video File")
        with st.spinner('Downloading...'):
            button = st.download_button(
                label="Download mp4",
                data=buffer,
                file_name=title_vid,
                mime="audio/mpeg")
            if button:
                st.success('Download Complete', icon="✅")
                st.balloons()