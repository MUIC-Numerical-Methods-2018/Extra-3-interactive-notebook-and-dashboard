import streamlit as st
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
from matplotlib import pyplot as plt

v = st.sidebar.slider('v', min_value=0., max_value=1., step=0.01)
replace_to = st.sidebar.slider('replace_to', min_value=0., max_value=1., step=0.01)

im = plt.imread('mario.png')
im = im[:,:,:3]
im_hsv = rgb_to_hsv(im)
def try_color_mask(v, replace_to):
    h = im_hsv[:, :, 0]
    red_mask = h < v

    copy_im = im_hsv.copy()
    copy_im[red_mask, 0] = replace_to
    fig, ax = plt.subplots()
    ax.imshow(hsv_to_rgb(copy_im))
    st.pyplot(fig)

try_color_mask(v, replace_to)

