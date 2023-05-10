import streamlit as st
from pytube import YouTube
import re
import tempfile

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"


def download_audio(url):
    global title_vid

    youtube_video = YouTube(url)
    title_vid = youtube_video.title

    with tempfile.NamedTemporaryFile(delete=True) as temp:
        file_path = temp.name + ".mp3"
        audio = youtube_video.streams.get_audio_only()
        audio.download(file_path)
        temp.close()

    return file_path


def get_info(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, type='video')
    details = {}
    details["image"] = yt.thumbnail_url
    details["streams"] = streams
    details["title"] = yt.title
    details["length"] = yt.length
    itag, resolutions, vformat, frate = ([] for i in range(4))
    for i in streams:
        res = re.search(r'(\d+)p', str(i))
        typ = re.search(r'video/(\w+)', str(i))
        fps = re.search(r'(\d+)fps', str(i))
        tag = re.search(r'(\d+)', str(i))
        itag.append(str(i)[tag.start():tag.end()])
        resolutions.append(str(i)[res.start():res.end()])
        vformat.append(str(i)[typ.start():typ.end()])
        frate.append(str(i)[fps.start():fps.end()])
    details["resolutions"] = resolutions
    details["itag"] = itag
    details["fps"] = frate
    details["format"] = vformat
    return details


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
    v_info = get_info(url)
    col1, col2 = st.columns([1, 1.5], gap="small")
    with st.container():
        with col1:
            st.image(v_info["image"])
        with col2:
            st.subheader("Video Details ⚙️")
            res_inp = st.selectbox(
                '__Select Resolution__', v_info["resolutions"])
            id = v_info["resolutions"].index(res_inp)
            st.write(f"__Title:__ {v_info['title']}")
            st.write(f"__Length:__ {v_info['length']} sec")
            st.write(f"__Resolution:__ {v_info['resolutions'][id]}")
            st.write(f"__Frame Rate:__ {v_info['fps'][id]}")
            st.write(f"__Format:__ {v_info['format'][id]}")
            file_name = st.text_input(
                '__Save as 🎯__', placeholder=v_info['title'])
            if file_name:
                if file_name != v_info['title']:
                    file_name
            else:
                file_name = v_info['title']

            if type == 'Video':
                file_name += ".mp4"
            else:
                file_name += ".mp3"

    button_v = st.button('view now')
    if button_v:
        st.video(url)

    button = st.button('Download now')
    if button:
        with st.spinner('Downloading...'):
            try:
                ds = v_info["streams"].get_by_itag(v_info['itag'][id])
                ds.download(filename=file_name, output_path="downloads/")
                st.success('Download Complete', icon="✅")
                st.balloons()
            except:
                st.error('Error: Save with a different name!', icon="🚨")
