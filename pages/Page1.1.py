import streamlit as st
import base64


#Code written by Ms.Mariann
#Opens a png file and turns it into a format that can be used on the website
#Need to import base64 for the code below to work
@st.cache_data()
def get_base64_of_bin_file(bin_file):
    '''
    Opens a png image file and converts it to a base64 string so it can be used by streamlit
    '''
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
#Uses the method above to display a background image
def set_png_as_page_bg(png_file):
    '''
    displays an image as a background
    code from: https://discuss.streamlit.io/t/how-do-i-use-a-background-image-on-streamlit/5067
    '''
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
      background-image: url("data:image/png;base64,%s");
      background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg("images/overall_background.png")


#Heading + icon
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)
with col2:
    st.markdown("<h1 style='text-align: left; color: #fefffc;'>INTRO TO TRIGONOMETRY</h1>", unsafe_allow_html=True)


#Code given by ChatGPT and fixed by Ms. Mariann
#Image/Button
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_base64 = get_image_base64("images/Tab 1.1 button.png")
#Image as button with redirect
with st.container():
    st.markdown(f"""
        <style>
        .img-button {{
            border: none;
            background-color: transparent;
            cursor: pointer;
        }}
        .img-button img {{
            width: 1000px;
            transition: transform 0.2s;
        }}
            .img-button img:hover {{
            transform: scale(1.05);
        }}
        </style>
        <a href='{"Page1_2"}'>
            <button class="img-button onclick="trig_page(); return true;">
                <img src="data:image/png;base64,{image_base64}" alt="CLICK TO START">
            </button>
        </a>
    """, unsafe_allow_html=True)