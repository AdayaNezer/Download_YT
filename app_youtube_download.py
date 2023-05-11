import streamlit as st
from pytube import YouTube
from down_audio import download_audio
from down_video import download_video


st.set_page_config(
    page_title="Download from YouTube",
    page_icon="https://www.svgrepo.com/show/421043/blog-premiere-public.svg",)

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

st.markdown('<h3>To download please enter a link</h3>',
            unsafe_allow_html=True)
url = st.text_input('')

st.markdown('<h3  ">Please select the file type</h3>',
            unsafe_allow_html=True)
type = st.radio('',
                ('Video', 'Audio'))

if type == 'Video':
    download_video(url)
else:
    download_audio(url)
