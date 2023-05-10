import streamlit as st
import pandas as pd
import numpy as np
from video_dl import download, download_audio
import base64


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
URL = st.text_input('')
st.markdown('<h3 style=" color: #e31072 ">Please select the file type</h3>',
            unsafe_allow_html=True)
type = st.radio('',
                ('Video', 'Audio'))

if st.button('Download now'):
    if type == 'Video':
        download(URL)
        st.markdown('<h3 color: #e31072 "> Downloaded successfully</h3>',
                    unsafe_allow_html=True)
    else:
        download_audio(URL)
        st.markdown('<h3 style=" color: #e31072 "> Downloaded successfully</h3>',
                    unsafe_allow_html=True)
