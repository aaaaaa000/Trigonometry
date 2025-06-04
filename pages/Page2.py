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


#Heading + icon
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/Icon_in_every_page_title_except_menu_page.png", caption=None, width=100)
with col2:
    st.markdown("<h2 style='text-align: left; color: #fefffc;'>EXIT GAME BY COMPLETING QUIZ</h2>", unsafe_allow_html=True)


#Space between title and questions
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)


#Text color and font made with the help of ChatGPT
#Content (questions and answers) written by ChatGPT
#Two Columns, each with a question and three answers (each with different answer explanation outputs)
col1, col2 = st.columns(2)
#Question 1
with col1:
    text = """
           <p style="font-family:sans-serif; color: #63d6ff; font-size: 20px;">
               QUESTION 1
            </p>
           """
    st.markdown(text, unsafe_allow_html=True)
    text = """
           <p style="font-family: sans-serif; color: #fefffc; font-size: 15px;">
               What is the sine of a 30° angle?
            </p>
           """
    st.markdown(text, unsafe_allow_html=True)
#Question 1 answer options with different outputs
    col1_, col2_, col3_ = st.columns(3)
    with col1_:
        if st.button("1"):
            st.write("Sorry, this is the wrong answer. The correct answer is 0.5 because in a right-angled triangle, the sine of an angle is defined as opposite side/adjacent side. Then, there is a common trigonometric ratios for 30°-60°-90° triangle. The sides of this triangle follow a consistent ratio: opposite 30°: 1, opposite 60°: √3, hypotenuse: 2. When we substitute sine=30 into the previous formula, we get sin(30)=1/2=0.5")
    with col2_:
        if st.button("√3"):
            st.write("Sorry, this is the wrong answer. The correct answer is 0.5 because in a right-angled triangle, the sine of an angle is defined as opposite side/adjacent side. Then, there is a common trigonometric ratios for 30°-60°-90° triangle. The sides of this triangle follow a consistent ratio: opposite 30°: 1, opposite 60°: √3, hypotenuse: 2. When we substitute sine=30 into the previous formula, we get sin(30)=1/2=0.5")
    with col3_:
        if st.button("0.5"):
            st.write("This is the correct answer! Congratulations!")
#Question 2
with col2:
    text = """
           <p style="font-family:sans-serif; color: #63d6ff; font-size: 20px;">
               QUESTION 2
            </p>
           """
    st.markdown(text, unsafe_allow_html=True)
    text = """
           <p style="font-family: sans-serif; color: #fefffc; font-size: 15px;">
               If sin(30°) = 0.5, what is the length of the opposite side in a right triangle where the hypotenuse is 10 cm?
            </p>
           """
    st.markdown(text, unsafe_allow_html=True)
# Question 2 answer options with different outputs
    col1_, col2_, col3_ = st.columns(3)
    with col1_:
        if st.button("5 cm"):
            st.write("This is the correct answer! Congratulations!")
    with col2_:
        if st.button("15 cm"):
            st.write("Sorry, this is the wrong answer. The correct answer is 5cm because when we use the sine formula sine(θ) = opposite side/adjacent side and when we substitute sine(30°) = 0.5 and hypotenuse = 10cm, we get 0.5 = opposite/10. Then, after multiplying both sides by 10, we get opposite = 0.5 x 10 = 5cm.")
    with col3_:
        if st.button("3 cm"):
            st.write("Sorry, this is the wrong answer. The correct answer is 5cm because when we use the sine formula sine(θ) = opposite side/adjacent side and when we substitute sine(30°) = 0.5 and hypotenuse = 10cm, we get 0.5 = opposite/10. Then, after multiplying both sides by 10, we get opposite = 0.5 x 10 = 5cm.")


#Space
col1_, col2_, col3_ = st.columns(3)


#ChatGPT note
text = """
           <p style="font-family: sans-serif; color: #fefffc; font-size: 10px;">
               *Content written by ChatGPT
            </p>
           """
st.markdown(text, unsafe_allow_html=True)