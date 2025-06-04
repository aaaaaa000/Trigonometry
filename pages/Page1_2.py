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


#Level up x1 heading + icon
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)
with col2:
    st.markdown("<h1 style='text-align: left; color: #fefffc;'>LEVEL UP x1</h1>", unsafe_allow_html=True)


#Text color and font made with the help of ChatGPT
#Content about trigonometry written by ChatGPT
#Level up x1 container (textbox) + content
with st.container(height=450, border=True):
    row1_col1, row1_col2 = st.columns([3,5])
    with row1_col1:
        st.image("images/Tab 1 picture 1.png", caption=None, width=300)
    with row1_col2:
        text = """
        <p style="font-family:sans-serif; color: #fefffc; font-size: 15px;">
            🌴 Alright! Let’s imagine you're standing outside and looking up at a tall tree. You can’t climb it to measure how tall it is, right? 
            But guess what — trigonometry is a kind of math that can help you figure out how tall that tree is without climbing it!
        </p>
        """
        st.markdown(text, unsafe_allow_html=True)
    col = st.columns(1)
    text = """
    <p style="font-family:sans-serif; color: #fefffc; font-size: 15px;">
        🔺 So, what is trigonometry?
        Trigonometry is the study of triangles, especially right-angled triangles (the ones with a 90° angle). It helps us understand the relationship between the angles and the sides of a triangle. Let’s break it down -- a right-angled triangle has:
     </p>
    """
    col[0].markdown(text, unsafe_allow_html=True)
    st.markdown("""
            <style>
                ol {
                    line-height: 1.2; /* Adjust line spacing */
                    color: #fefffc; /* Change text color */
                    font-family: sans-serif; /* Change font */
                    font-size: 10px; /* Change font size */
                }
            </style>
            <ol>
                <li>One right angle (90 degrees)</li>
                <li>Three sides</li>
            </ol>
            """, unsafe_allow_html=True)
    st.markdown("""
            <style>
                ul {
                     list-style-type: none; /* Remove bullet points */
                     line-height: 1.1; /* Adjust line spacing */
                     color: #fefffc; /* Change text color */
                     font-family: sans-serif; /* Change font */
                     font-size: 10px; /* Change font size */
                }
            </style>
            <ul>
                <li>a. The hypotenuse (the longest side, across from the right angle)</li>
                <li>b. The opposite side (across from the angle you're looking at)</li>
                <li>c. The adjacent side (next to the angle you're looking at)</li>
            </ul>
            """, unsafe_allow_html=True)
    col = st.columns(1)
    text = """
            <p style="font-family:sans-serif; color: #fefffc; font-size: 10px;">
                *Content written by ChatGPT
             </p>
            """
    col[0].markdown(text, unsafe_allow_html=True)


#Space
row1_col1, row1_col2 = st.columns(2)


#Level up x2 heading + icon
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)
with col2:
    st.markdown("<h1 style='text-align: left; color: #fefffc;'>LEVEL UP x2</h1>", unsafe_allow_html=True)


#Text color and font made with the help of ChatGPT
#Level up x2 container (textbox) + content
with st.container(height=300, border=True):
    row1_col1, row1_col2 = st.columns([3,5])
    with row1_col1:
        st.image("images/Tab 1 picture 2.png", caption=None, width=300)
    with row1_col2:
        text = """
        <p style="font-family:sans-serif; color: #fefffc; font-size: 15px;">
            📐 Key Idea: Ratios!
            Trigonometry is all about comparing sides using ratios.
            There are 3 main ones to remember, and they sound like this:
            1. Sine (sin) = Opposite / Hypotenuse
            2. Cosine (cos) = Adjacent / Hypotenuse
            3. Tangent (tan) = Opposite / Adjacent
        </p>
        """
        st.markdown(text, unsafe_allow_html=True)
    col = st.columns(1)
    text = """
    <p style="font-family:sans-serif; color: #fefffc; font-size: 15px;">
        🧠 Easy way to remember -- using the acronym SOH-CAH-TOA!
     </p>
    """
    col[0].markdown(text, unsafe_allow_html=True)
    col = st.columns(1)
    text = """
    <p style="font-family:sans-serif; color: #fefffc; font-size: 15px;">
        📏 Additionally, why is trigonometry useful?
        Trigonometry is used in: engineering and design, video game development, astronomy, building and construction, and even in things like music and sports!
     </p>
    """
    col[0].markdown(text, unsafe_allow_html=True)
    col = st.columns(1)
    text = """
            <p style="font-family:sans-serif; color: #fefffc; font-size: 10px;">
                *Content written by ChatGPT
             </p>
            """
    col[0].markdown(text, unsafe_allow_html=True)