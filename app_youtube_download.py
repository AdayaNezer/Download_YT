import streamlit as st
from pytube import YouTube
import os

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"


# def download(video_url):
#     video = YouTube(video_url)
#     st.write("Title of Video: " + str(video.title))
#     st.write("Number of Views: " + str(video.views))
#     video = video.streams.get_highest_resolution()

#     try:
#         # st.download_button(
#         #     label="Download data",
#         #     data=video.download(),
#         #     file_name=f'vvv.mp4',
#         # )
#         video.download()
#     except:
#         print("Failed to download video")

#     print("video was downloaded successfully")


# def download_audio(video_url):
#     video = YouTube(video_url)
#     st.write("Title of Video: " + str(video.title))
#     st.write("Number of Views: " + str(video.views))
#     audio = video.streams.filter(only_audio=True, file_extension='mp4').first()

#     try:
#         video.streams.get_audio_only().download()
#         audio.download(os.path.expanduser("~/Downloads"))
#     except:
#         print("Failed to download audio")

#     print("audio was downloaded successfully")


st.markdown(
    f"""
         <style>
         .stApp {{
             background: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v546batch3-mynt-34-badgewatercolor_1.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=89288ef4b47127f7f34a5998b50e4470.jpg");
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)

st.markdown('<h1 style="color: #e31072 ">Download videos and songs from YouTube</h1>',
            unsafe_allow_html=True)

st.markdown('<h3 style=" color: #e31072 ">To download please enter a link</h3>',
            unsafe_allow_html=True)
url = st.text_input('')

st.markdown('<h3 style=" color: #e31072 ">Please select the file type</h3>',
            unsafe_allow_html=True)
type = st.radio('',
                ('Video', 'Audio'))
if url != '':
    video = YouTube(url)
    st.markdown(
        f'<h3 style=" color: #e31072 ">Title of Video:</h3> <h5> { str(video.title)} </h5>', unsafe_allow_html=True)
    st.markdown(
        f'<h3 style=" color: #e31072 ">Number of Views:</h3> <h5>  { str(video.views)}</h5>', unsafe_allow_html=True)
    st.video(url)
    if st.button('Download now'):
        if type == 'Video':
            video.streams.get_highest_resolution().download()

        else:
            video.streams.get_audio_only().download()
    print("video was downloaded successfully")

    st.markdown('<h3 style= color: " #e31072 "> Downloaded successfully</h3>',
                unsafe_allow_html=True)
