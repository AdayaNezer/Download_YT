import streamlit as st
# import instaloader
from io import BytesIO
from pathlib import Path


# @st.cache(show_spinner=False, persist=True)
# def download_video_to_buffer(url):
#     try:
#         buffer = BytesIO()
#         loader = instaloader.Instaloader()
#         post = instaloader.Post.from_shortcode(
#             loader.context, url.split("/")[-2])
#         if post.typename == "GraphVideo":
#             loader.download_post(post, target='.')
#             downloaded_filename = f"{post.owner_username}_{post.date_utc}_{post.shortcode}.mp4"
#             file_path = Path(".") / downloaded_filename
#             buffer.write(file_path.read_bytes())
#             return downloaded_filename, buffer
#         else:
#             return None, None
#     except Exception as e:
#         return None, str(e)


# def download_video_ins(url):
#     if url != '':
#         with st.spinner("Downloading video from Instagram..."):
#             default_filename, buffer = download_video_to_buffer(url)
#             if default_filename is None or buffer is None:
#                 st.error(f"Failed to download the video: {buffer}")
#                 return

#         st.subheader("Title")
#         st.write(default_filename)
#         st.subheader("Watch the video")
#         st.video(buffer, format='video/mp4')
#         st.subheader("Download video File")

#         # Provide a direct download link to the user
#         st.markdown(get_binary_file_downloader_html(
#             buffer, default_filename), unsafe_allow_html=True)


# def get_binary_file_downloader_html(bin_file, file_label='File'):
#     # Function to generate a direct download link
#     bin_data = bin_file.getvalue()
#     b64 = b64encode(bin_data).decode()
#     href = f'<a href="data:file/mp4;base64,{b64}" download="{file_label}">Click here to download</a>'
#     return href


# url = st.text_input("Enter Instagram Video URL")
# if st.button("Download"):
#     download_video(url)
