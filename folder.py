import streamlit as st
import os
import glob
import uuid

b1 = st.button("作成")
b2 = st.button("消去")

if b1:
    x = str(uuid.uuid1())
    with open(f"scr/{x}", 'w') as f:
        pass
if b2:
    y = glob.glob("scr/*")
    for i in y:
        os.remove()

st.write(glob.glob(f'{os.path.dirname(__file__)}'))
st.write(glob.glob("scr/*"))
st.write(glob.glob("test/*"))
