import streamlit as st
from down_audio import download_audio
from down_video import download_video
from down_inst import download_video_ins


def start():
    st.markdown('<h1 style="color: #f08080 ">Download videos and songs from YouTube</h1>',
                unsafe_allow_html=True)

    st.markdown('<h3>To download please enter a link</h3>',
                unsafe_allow_html=True)
    url = st.text_input('please here', label_visibility="hidden")

    st.markdown('<h3>Please select the file type</h3>',
                unsafe_allow_html=True)
    type = st.radio('please here',
                    ('Video', 'Audio'), label_visibility="hidden")

    if type == 'Video':
        download_video(url)
    else:
        download_audio(url)


def about():
    True
    # st.markdown('<h1 style="color: #f08080 ">Download videos and songs from Instagram</h1>',
    
    #             unsafe_allow_html=True)

    # st.markdown('<h3>To download please enter a link</h3>',
    #             unsafe_allow_html=True)
    # url = st.text_input('please here', label_visibility="hidden")
    # download_video(url)
