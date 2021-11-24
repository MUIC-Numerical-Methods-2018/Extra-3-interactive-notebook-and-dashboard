import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

min_red = st.sidebar.slider('min_red', min_value=0., max_value=1., step=0.1)
max_red = st.sidebar.slider('max_red', min_value=0., max_value=1., step=0.1)

new_hue = st.sidebar.slider('new hue', min_value=0., max_value=1., step = 0.1)

im = plt.imread('mario.png')

# need to transform it first
plt.imshow(im)
st.pyplot(plt.gcf())

