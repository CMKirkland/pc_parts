import streamlit as st
from streamlit import session_state as ss
from PIL import Image

def render():
    st.title("On this page you can see all of the hard drives that we offer.")
price2= []
def button6():
    if st.button('view price', key = 55):
        price2.append(49.99)
        st.write("The price is $49.99")

def button7():
    if st.button('view price', key = 56):
        price2.append(119.99)
        st.write("The price is $119.99")

def button8():
     if st.button('view price', key = 57):
        price2.append(224.99)
        st.write("The price is $224.99")

def button9():
    if st.button('view price', key = 58):
        price2.append(129.99)
        st.write("The price is $129.99")

def button10():
    if st.button('view price', key = 59):
        price2.append(74.99)
        st.write("The price is $74.99")


def display_hard_drive1():
    #49.99
    st.header("Seagate BarraCuda 1TB 5400 RPM SATA III 6Gb/s 2.5 in Internal SMR Hard Drive")
    hard_drive1 = Image.open('./pages/hard_drive1.jpg')
    st.image(hard_drive1, caption='')
    hard_drive1_price = 49.99
    if st.button("view specs", key = 6):
        st.markdown("2.5in , SATA 3.0 6.0Gb/s, 5,400 RPM, 128MB")
  

def display_hard_drive2():
    #119.99
    st.header("Seagate BarraCuda 8TB 5400 RPM SATA III 6Gb/s 3.5 in OEM Internal SMR Hard Drive")
    hard_drive2 = Image.open('./pages/hard_drive2.jpg')
    st.image(hard_drive2, caption='')
    hard_drive2_price = 119.99 
    if st.button("view specs", key = 7):
        st.markdown("3.5in, SATA 3.0 6.0Gb/s, 5,400 RPM, 256MB")
 

def display_hard_drive3():
    #224.99
    st.header("Seagate FireCuda 8TB 7200 RPM SATA III 6Gb/s 3.5 in Internal CMR Hard Drive")
    hard_drive3 = Image.open('./pages/hard_drive3.jpg')
    st.image(hard_drive3, caption='')
    hard_drive3_price = 224.99
    if st.button("view specs", key = 8):
        st.markdown("3.5 in, SATA 3.0 6.0Gb/s, 7,200 RPM, 256MB")
  

def display_hard_drive4():
    #129.99
    st.header("Seagate FireCuda 4TB 7200 RPM SATA III 6Gb/s 3.5 in Internal CMR Hard Drive")
    hard_drive4 = Image.open('./pages/hard_drive4.jpg')
    st.image(hard_drive4, caption='')
    hard_drive4_price = 129.99
    if st.button("view specs", key = 9):
        st.markdown("3.5 in, SATA 3.0 6.0Gb/s, 7,200 RPM, 256MB")
   

def display_hard_drive5():
    #74.99
    st.header("Seagate Barracuda 2TB 5400 RPM SATA III 6Gb/s 2.5 in Internal SMR Hard Drive")
    hard_drive5 = Image.open('./pages/hard_drive5.jpg')
    st.image(hard_drive5, caption='')
    hard_drive5_price = 74.99
    if st.button("view specs", key = 10):
        st.markdown("2.5 in, SATA 3.0 6.0Gb/s, 5,400 RPM, 128MB")
 

render()
display_hard_drive1()
button6()
display_hard_drive2()
button7()
display_hard_drive3()
button8()
display_hard_drive4()
button9()
display_hard_drive5()
button10()