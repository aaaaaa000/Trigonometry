import base64
import streamlit as st


#Code given by Ms.Mariann
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

col1, col2, col3 = st.columns([1, 10, 1])
with col2:
    #Code partially given by ChatGPT
    #Heading Icon
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col2:
        st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)

    row2_col1, row2_col2 = st.columns(2)

    #Heading
    st.markdown("<h1 style='text-align: center; color: #fefffc;'>MATH GAMING CENTER</h1>", unsafe_allow_html=True)

    #"Sign in" button
    #Code mostly given by ChatGPT and fixed by Ms. Mariann
    left, center, right = st.columns([1, 2, 1])
    with center:
        def get_image_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        image_base64 = get_image_base64("images/Home page button.png")
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
                    width: 200px;
                    transition: transform 0.2s;
                }}
                    .img-button img:hover {{
                    transform: scale(1.05);
                }}
                </style>
                <a href='{"MenuPage"}'>
                    <button class="img-button onclick="trig_page(); return true;">
                        <img src="data:image/png;base64,{image_base64}" alt="CLICK TO START">
                    </button>
                </a>
            """, unsafe_allow_html=True)