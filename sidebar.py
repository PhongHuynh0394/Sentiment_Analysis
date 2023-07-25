import streamlit as st
from streamlit_option_menu import option_menu


def show():
    with st.sidebar:
        st.markdown("""
                    # Applications
                    """, unsafe_allow_html = False)
        selected = option_menu(
            menu_title = "Main Menu", #required
            
            options = ["Home","Idea 1", "Idea 2"], #required
            icons = ["home","card-text", "card-text"], #optional
            
            # menu_icon="cast", #optional
            default_index = 0, #optional
        )
        return selected