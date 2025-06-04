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


#Heading + align to center
st.markdown("<h1 style='text-align: center; color: #fefffc;'>Menu Page</h1>", unsafe_allow_html=True)


#Columns for page 1, 2, and 3
col1, col2, col3 = st.columns(3, border=True)
#Custom CSS for column styling
st.markdown("""
    <style>
    div[data-testid="column"] {
        border: 3px solid #bad8f5;  /* color: #bad8f5, thickness: 5px */
        margin: 5px;
    }
    </style>
    """, unsafe_allow_html=True)


#Columns content
with col1:
    st.image("images/Menu page 1 picture.png")
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 25px;">Page 1</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Basic definition and memorization tips</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    container = st.container(border=True)
    st.page_link("pages/Page1.1.py", label="Check it out", icon="👀")
with col2:
    st.image("images/Menu page 2 picture.png")
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 25px;">Page 2</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Exit quiz</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.page_link("pages/Page2.py", label="Check it out", icon="👀")
with col3:
    st.image("images/Menu page 3 picture.png")
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 25px;">Page 3</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Available resources to assist learning</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.page_link("pages/Page3.py", label="Check it out", icon="👀")