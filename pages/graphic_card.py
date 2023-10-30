import streamlit as st
from streamlit import session_state as ss
from PIL import Image
def welcome2():
    st.title("Welcome to the graphics card page")
    st.text("here you will find different graphics cards with their specs and prices.")

price =[]
def button1():
  if st.button('view price', key = 50):
      price.append(799.99)
      st.write("The price is $799.99")

def button2():
  if st.button('view price', key = 51):
      price.append(2199.99)
      st.write("The price is $2,199.99")

def button3():
   if st.button('view price', key = 52):
      price.append(549.99)
      st.write("The price is $549.99")

def button4():
  if st.button('view price', key = 53):
      price.append(1819.99)
      st.write("The price is $1,819.99")

def button5():
  if st.button('view price', key = 54):
      price.append(799.99)
      st.write("The price is $799.99")


def gcard1_image():
    image1 = Image.open('./pages/graphiccard1.jpg')
    st.image(image1, caption='')

def gcard1_info():
    st.header("Gigabyte NVIDIA GeForce RTX 4070 Ti Windforce Overclocked Triple Fan 12GB GDDR6X PCIe 4.0 Graphics Card")
    gcard1_image()
    gcard1_price = 799.99
    if st.button("view specs", key =1):
        st.markdown(" Specs:\n 12GB GDDR6X 192-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Triple Slot \n DisplayPort 1.4 HDMI 2.1")
    

def gcard2_image():
    Image2 = Image.open('./pages/graphiccard2.jpg')
    st.image(Image2, caption='')

def gcard2_info():
    st.header("ASUS NVIDIA GeForce RTX 4090 ROG Strix LC Overclocked Liquid Cooled 24GB GDDR6X PCIe 4.0 Graphics Card")
    gcard2_image()
    gcard2_price = 2199.99
    if st.button("view specs", key = 2):
        st.markdown("24GB GDDR6X 384-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Triple Slot \n DisplayPort 1.4a, HDMI 2.1a")
  
def gcard3_image():
    image3 = Image.open('./pages/graphiccard3.jpg')
    st.image(image3, caption='')

def gcard3_info():
    st.header("Zotac NVIDIA GeForce RTX 4070 Twin Edge Spider-Man Across the Spider-Verse Bundle Overclocked Dual Fan 12GB GDDR6X PCIe 4.0 Graphics Card")
    gcard3_image()
    gcard3_price = 549.99
    if st.button("view specs", key = 3):
        st.markdown("specs:\n12GB GDDR6X 192-bit Memory \n7680 x 4320 Maximum Resolution \nPCIe 4.0 \nFull Height, Dual Slot \nDisplayPort 1.4a, HDMI 2.1")
    
def gcard4_image():
    Image4 = Image.open('./pages/graphiccard4.jpg')
    st.image(Image4, caption='')
    
def gcard4_info():
    st.header("ASUS NVIDIA GeForce RTX 4090 TUF Gaming Overclocked Triple Fan 24GB GDDR6 PCIe 4.0 Graphics Card")
    gcard4_image()
    gcard4_price = 1819.99
    if st.button("view specs", key = 4):
        st.markdown("specs: \n24GB GDDR6X 384-bit Memory \n 7680 x 4320 Maximum Resolution \n PCIe 4.0 \n Full Height, Quad Slot \n DisplayPort 1.4a, HDMI 2.1a")
   
def gcard5_image():
    image5 = Image.open('./pages/graphiccard5.jpg')
    st.image(image5, caption='')

def gcard5_info():
    st.header('EVGA NVIDIA GeForce RTX 3080 Ti FTW3 Ultra Gaming Triple-Fan 12GB GDDR6X PCIe 4.0 Graphics Card (Refurbished)')
    gcard5_image()
    gcard5_price = 799.99
    if st.button("view specs", key = 5):
        st.markdown("specs \n12GB GDDR6X 384-bit Memory \n7680 x 4320 Maximum Resolution \nPCIe 4.0 \nFull Height, Triple Slot \nDisplayPort 1.4a, HDMI 2.1")
   

def showpage():
    welcome2()
    gcard1_info()
    button1()
    gcard2_info()
    button2()
    gcard3_info()
    button3()
    gcard4_info()
    button4()
    gcard5_info()
    button5()

showpage()