import streamlit as st


# Code given by Ms.Mariann
# Opens a png file and turns it into a format that can be used on the website
# Need to import base64 for the code below to work
@st.cache_data()
def get_base64_of_bin_file(bin_file):
    '''
    Opens a png image file and converts it to a base64 string so it can be used by streamlit
    '''
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Uses the method above to display a background image
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


# Helpful Resources + icon
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)
with col2:
    st.markdown("<h1 style='text-align: left; color: #fefffc;'>HELPFUL RESOURCES</h1>", unsafe_allow_html=True)


# Space
col1_, col2_, col3_ = st.columns(3)


#from PIL import Image
#import base64

# Function to convert an image to base64
#def get_base64_of_bin_file(bin_file):
    #with open(bin_file, 'rb') as f:
        #data = f.read()
    #return base64.b64encode(data).decode()

# Path to the image file
#image_path = "images/Tab 3 picture 1.png"
#image_base64 = get_base64_of_bin_file(image_path)

# Create a container that spans the entire width
#st.markdown("""
#<style>
    #.stContainer {
        #display: flex;
        #flex-direction: row;
        #align-items: center;
        #justify-content: space-between;
        #border: 2px solid white;
        #padding: 10px;
        #border-radius: 0px;
        #background-color: transparent; /* No background color */
    #}
    #.image-container {
        #flex: 1;
        #text-align: center;
    #}
    #.content-container {
        #flex: 2;
        #padding-left: 20px;
    #}
#</style>
#""", unsafe_allow_html=True)


# Create two columns for Khan Academy
col1, col2 = st.columns([1, 2])
with col1:
    st.image ("images/Tab 3 picture 1.png")
    #<div class="image-container">
        #<img src="data:image/png;base64,{image_base64}" alt="Girl in a jacket" width="400" height="100">
    #</div>
    #""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="content-container">
        <p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Benefits of Khan Academy:</p>
        <style>
            ul {
                line-height: 1; /* Adjust line spacing */
                color: #fefffc; /* Change text color */
                font-family: sans-serif; /* Change font */
                font-size: 9px; /* Change font size */
            }
        </style>
        <ul>
            <li>Informative videos</li>
            <li>Interactive practices and detailed answer explanations</li>
            <li>Available discussion forum with a supportive community of learners</li>
        </ul>
        <p><a href="https://www.khanacademy.org/" target="_blank">GO TO WEBSITE</a></p>
    </div>
    """, unsafe_allow_html=True)


# Create two columns for Math is Fun
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/Tab 3 picture 2.png")
with col2:
    st.markdown("""
        <p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Benefits of Math is Fun:</p>
        <style>
            ul {
                line-height: 1; /* Adjust line spacing */
                color: #fefffc; /* Change text color */
                font-family: sans-serif; /* Change font */
                font-size: 9px; /* Change font size */
            }
        </style>
        <ul>
            <li>Simple, easy-to-understand explanations</li>
            <li>Visual explanations</li>
            <li>Offers games and puzzles to support learning</li>
        </ul>
        <p><a href="https://www.mathsisfun.com/" target="_blank">GO TO WEBSITE</a></p>
    </div>
    """, unsafe_allow_html=True)


# Create two columns for IXL
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/Tab 3 picture 3.png")
with col2:
    st.markdown("""
        <p style="font-family:sans-serif; color:#fefffc; font-size: 15px;">Benefits of IXL:</p>
        <style>
            ul {
                line-height: 1; /* Adjust line spacing */
                color: #fefffc; /* Change text color */
                font-family: sans-serif; /* Change font */
                font-size: 9px; /* Change font size */
            }
        </style>
        <ul>
            <li>Personalized practice questions</li>
            <li>A variety of topics</li>
            <li>Detailed answer explanations</li>
        </ul>
        <p><a href="https://www.ixl.com/?partner=google&campaign=71589568&adGroup=129630700247&gad_source=1&gad_campaignid=71589568&gbraid=0AAAAADrr3AphboFIhlK4dHYqrGs9Z3_Iu&gclid=CjwKCAjw6NrBBhB6EiwAvnT_rg_elFM124RTESZNdI2iR2bV_J-zxViviRRjJF7BllH00AahBpotEBoCv4oQAvD_BwEstream" target="_blank">GO TO WEBSITE</a></p>
    </div>
    """, unsafe_allow_html=True)