import streamlit as st
from down_audio import download_audio
from down_video import download_video


def start():
    st.markdown('<h1 style="color: #f08080 ">Download videos and songs from YouTube</h1>',
                unsafe_allow_html=True)

    st.markdown('<h3>To download please enter a link</h3>',
                unsafe_allow_html=True)
    url = st.text_input('')

    st.markdown('<h3>Please select the file type</h3>',
                unsafe_allow_html=True)
    type = st.radio('---Here---',
                    ('Video', 'Audio'))

    if type == 'Video':
        download_video(url)
    else:
        download_audio(url)


def about():
    st.markdown('''<h1 style="color: #f08080 ">Hi</h1>''',
                unsafe_allow_html=True)
    st.snow()
