import streamlit as st
from streamlit import session_state as ss
from PIL import Image

if 'page' not in ss:
    ss['page']=0
def welcome():
    st.title("Computer Parts Picker")
    st.header("This website is for building a potential PC. It'll help you compare parts and set a budget.")
    st.markdown("This was made by two people that know nothing about computers so we may be wrong.")
    setup = Image.open('C:/Users/CMKirkland/Documents/pc_parts/pages/setup.jpg')
    st.image(setup, caption='This an example of what your set up could look like.')
    st.markdown("Select the sidebar to view the different parts of the computer.")
    st.write("[Pc]( https://starforgesystems.com/pages/our-creators)")
    st.write("[Hard drives, graphics cards, and cases](https://www.microcenter.com/site/products/computer-parts.aspx)")
    st.write("[Mice](https://www.newegg.com/)")
    st.write("[Keyboards](https://mechanicalkeyboards.com/)")



def main():
       welcome()

if __name__ == '__main__':
    main()