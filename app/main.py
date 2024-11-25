import streamlit as st



# Page config
st.set_page_config(
    page_title="Sentiment analysis",
    page_icon="😀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
import sidebar as sidebar
import idea_1 as idea_1
import idea_2 as idea_2
import home as home
import nltk
nltk.download('stopwords')

# Show page
page = sidebar.show()

# Each page
if page=="Home":
    home.renderPage()
elif page=="Idea 1":
    idea_1.renderPage()
elif page=="Idea 2":
    idea_2.renderPage()
