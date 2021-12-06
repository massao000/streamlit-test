import streamlit as st
import os
import glob
import uuid

b1 = st.button("test")

if b1:
    x = str(uuid.uuid1())
    with open(f"scr/{x}", 'w') as f:
        pass


st.write(glob.glob(f'{os.path.dirname(__file__)}'))
st.write(glob.glob("scr/*"))
st.write(glob.glob("test/*"))
