import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

min_red = st.sidebar.slider('min_red', value= 0.01, min_value=0., max_value=1., step=0.01)
max_red = st.sidebar.slider('max_red', value=0.8, min_value=0., max_value=1., step=0.01)

new_hue = st.sidebar.slider('new hue', min_value=0., max_value=1., step = 0.01)

# need to transform it firstimport numpy as np
im = plt.imread('mario.png')
im_rgb = im[:, :, :3]
hsv = mpl.colors.rgb_to_hsv(im_rgb)
print(max_red, min_red, new_hue)
mask = (hsv[:,:,0] > max_red) | (hsv[:,:,0] < min_red)
hsv[mask, 0] = new_hue
new_rgb = mpl.colors.hsv_to_rgb(hsv)
plt.imshow(new_rgb)

# fill in here
st.pyplot(plt.gcf())

