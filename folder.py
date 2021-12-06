import streamlit as st
import os
import glob
import uuid
import re

b1 = st.button("作成")
b2 = st.button("消去")
file = st.file_uploader("", type=["mp3", 'wav', "mp4"])
st.audio(file)
st.write(file)
if b1:
    x = str(uuid.uuid1())
    with open(f"scr/{file.name}", 'w') as f:
        pass
if b2:
    y = glob.glob("scr/*")
    for i in y:
        os.remove(i)

st.write(glob.glob(f'{os.path.dirname(__file__)}'))
st.write(glob.glob("scr/*"))
st.write(glob.glob("test/*"))

for i in glob.glob(f"scr/*"):
    m = re.compile("mp3" | "mp4" | "wav")
    st.write(m.match.group())
    # st.write(m.group())
    # st.audio(m.group())
