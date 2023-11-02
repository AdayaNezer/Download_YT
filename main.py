import download_menu
import streamlit as st

# st.set_page_config(
#     page_title="Download from YouTube",
#     page_icon="https://www.svgrepo.com/show/421043/blog-premiere-public.svg",
# )

from navbar import get_current_route, inject_custom_css, navbar_component



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


inject_custom_css()
navbar_component()
st.set_option('deprecation.showPyplotGlobalUse', False)


def navigation():
    route = get_current_route()
    if route == "home":
        download_menu.start()
    elif route == "about":
        download_menu.about()
    elif route == None:
        download_menu.start()


navigation()
