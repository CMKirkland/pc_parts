import streamlit as st
from streamlit import session_state as ss
from PIL import Image

def render():
    st.title("On this page you can see all of the mice that we offer.")
price4 =[]
def button16():
    if st.button('view price', key = 70):
        price4.append(24.99)
        st.write("The price is $24.99")

def button17():
    if st.button('view price', key = 71):
        price4.append(159.99)
        st.write("The price is $159.99")

def button18():
     if st.button('view price', key = 72):
        price4.append(19.99)
        st.write("The price is $19.99")

def button19():
    if st.button('view price', key = 73):
        price4.append(157.99)
        st.write("The price is 157.99")

def button20():
    if st.button('view price', key = 74):
        price4.append(79.99)
        st.write("The price is 79.99")

def display_mouse1():
    #24.99
    st.header("EVGA X20 Gaming Mouse, Wireless, Grey, Customizable, 16,000 DPI, 5 Profiles, 10 Buttons, Ergonomic 903-T1-20GR-KR")
    mouse1 = Image.open('./mouse1.jpg')
    st.image(mouse1, caption='')
    mouse1_price = 24.99
    if st.button("View specs", key = 16):
        st.markdown("Triple Sensor 3-Dimension Array Tech, Quick Responding Mechanism, On the fly DPI Settings + 5 Onboard Profiles, Ergomic Design with Sniper Button, 3 Modes of connection 2.4Ghz / Bluetooth / USB wired")
  
def display_mouse2():
    #159.99
    st.header("Razer Basilisk V3 Pro Customizable Wireless Gaming Mouse: Fast Optical Switches Gen-3 - HyperScroll Tilt Wheel - Chroma RGB - 11 Programmable Buttons - Focus Pro 30K Optical Sensor - Classic Black")
    mouse2 = Image.open('./pages/mouse2.jpg')
    st.image(mouse2, caption='')
    mouse2_price = 159.99
    if st.button("View specs", key = 17):
        st.markdown("Iconic Ergonomic Form with 10+1 Programmable Buttons: Favored by millions worldwide, the mouse’s signature shape perfectly supports cutting edge ergonomics and endless customizability options, 13-Zone Chroma Lighting with Full Underglow: Customize each zone from over 16.8 million colors and countless lighting effects, and experience greater immersion as they react dynamically with over 150 Chroma-integrated games, Razer Focus Pro 30K Optical Sensor: Razer’s brand-new sensor provides flawless tracking performance on a wider variety of surfaces including glass—supported by intelligent functions for enhanced aim and control, Razer Optical Mouse Switches Gen-3: From an improved 90-million click lifecycle with zero double-clicking issues, to a blistering 0.2ms actuation with no debounce delay, enjoy reliability and speed that outshines all others, Razer HyperSpeed Wireless: Enjoy ultra-responsive gaming with speeds 25% faster than other wireless tech.")
  
def display_mouse3():
    #19.99
    st.header("MSI Clutch GM08 Gaming Mouse, 4200 DPI, Optical Sensor, 3 Adjustable Weights, Red LED Lighting, Symmetrical Design")
    mouse3 = Image.open('./mouse3.jpg')
    st.image(mouse3, caption='')
    mouse3_price = 19.99
    if st.button("View specs", key = 18):
        st.markdown("Durable Gaming Switches with 10M+ Clicks, PixArt PAW3519 Optical Sensor, up to 4200 DPI, Precise Scroll Wheel, MSI Dragon LED, Adjustable Weight System Inside, Dragon Scale Grips, Polygonal Side Buttons, Buttom LED Lighting, Palm and Claw Grip")
   
def display_mouse4():
    #157.99
    st.header("Logitech G502 X PLUS LIGHTSPEED Wireless RGB Gaming Mouse - Optical mouse with LIGHTFORCE hybrid switches, LIGHTSYNC RGB, HERO 25K gaming sensor, compatible with PC - macOS/Windows - White")
    mouse4 = Image.open('./mouse4.jpg')
    st.image(mouse4, caption='')
    mouse4_price = 157.99
    if st.button("View specs", key = 19):
        st.markdown("Icon reinvented: From the legacy of Logitech's most popular G502 design, G502 X LIGHTSPEED wireless gaming mouse is reimagined and redesigned with the latest innovations in gaming technology, LIGHTFORCE switches: All-new hybrid optical-mechanical switch technology for incredible speed and reliability, as well as precise actuation with crisp response, for hours of performance gaming, LIGHTSPEED wireless: This wireless mouse features pro-grade connectivity, with an updated protocol achieving a 68 percent faster response rate than the previous generation and improved reliability, HERO 25K gaming sensor: Incredibly precise down to the sub-micron for high-precision accuracy with zero smoothing/filtering/acceleration for high gaming performance every time on the computer, Redesigned DPI-shift button: This cordless optical gaming mouse features a reversible and removable DPI-shift button for precise customization depending on your grip and preference")
  
def display_mouse5():
    #79.99
    st.header("Corsair SCIMITAR RGB ELITE CH-9304211-NA Black 17 Buttons 1 x Wheel USB 2.0 Type-A Wired Optical 18000 dpi MOBA/MMO Gaming Mouse, Backlit RGB LED")
    mouse5 = Image.open('./mouse5.jpg')
    st.image(mouse5, caption='')
    mouse5_price = 79.99
    if st.button("View specs", key = 20):
        st.markdown("Loaded with 17 fully programmable buttons, ideal for performing frequent actions and executing complex macros in MMOs and MOBAs. Unique Key Slider control system lets you reposition the 12 side buttons to comfortably fit your grip. Equipped with a custom PixArt PMW3391 native 18,000 DPI optical sensor, adjustable in 1 DPI resolution steps, for highly accurate and customizable tracking. The SCIMITAR RGB ELITE's 50 million click-rated Omron switches, durably constructed scroll wheel, and braided cable ensure that it stands up to the wear-and-tear of extended gaming. Sculpted to comfortably fit the contours of your palm, regardless of hand size or grip style, with a right-side finger rest for added support. Dynamic RGB backlighting with near limitless customization across four lighting zones. Powerful CORSAIR iCUE software enables RGB lighting control, sophisticated macro programming and button remaps, sensitivity customization, surface calibration, and more.")
  
render()
display_mouse1()
button16()
display_mouse2()
button17()
display_mouse3()
button18()
display_mouse4()
button19()
display_mouse5()
button20()