import streamlit as st


st.set_page_config(
    page_title="Download from YouTube",
    page_icon="https://www.svgrepo.com/show/421043/blog-premiere-public.svg",
)

import download_menu
from navbar import get_current_route, inject_custom_css, navbar_component

st.markdown(
    f"""
            <style>
            .stApp {{
                background: url("https://images.rawpixel.com/image_social_landscape/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm00MjItMDYzLWt6cGhnMjNrLmpwZw.jpg");
                background-size: cover
            }}
            </style>
            """,
    unsafe_allow_html=True
)


inject_custom_css()
navbar_component()
st.set_option('deprecation.showPyplotGlobalUse', False)


def navigation():
    route = get_current_route()
    if route == "home":
        download_menu.start()
    else:
        download_menu.start()


navigation()
