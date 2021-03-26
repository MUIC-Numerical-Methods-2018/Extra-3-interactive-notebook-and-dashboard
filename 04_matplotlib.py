import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

m = st.sidebar.slider('m', min_value=-1., max_value=1., step=0.1)
c = st.sidebar.slider('c', min_value=-1., max_value=1., step=0.1)
xs = np.linspace(0,1, 100)
ys = m * xs + c

fig, ax = plt.subplots()
ax.plot(xs, ys)
ax.set_ylim(-2,2)

st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(xs, xs**2)

st.pyplot(fig)

