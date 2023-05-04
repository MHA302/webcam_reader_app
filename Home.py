import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    u_img = Image.open(uploaded_image)
    g_img = u_img.convert("L")
    st.image(g_img)

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)
    # convert the image into grayscale
    gray_img = img.convert("L")
    # render the grayscale image on the webpage
    st.image(gray_img)
