import streamlit as st
import numpy as np
import time
import pandas as pd

text = ("""One sunny morning, as Elara was wandering through the Whispering Woods, she came across a tiny squirrel named Nutmeg. Nutmeg was in a state of distress, chattering anxiously and flicking her bushy tail. When Elara asked what was wrong, Nutmeg explained that the annual Great Nut Gathering contest was just a day away, and the prized Golden Acorn had mysteriously vanished.""")

def stream_data(data):
    for word in data.split():
        yield word + " "
        time.sleep(0.1)

prompt = st.chat_input("Say Something")

if prompt:
    with st.chat_message("human"):
        st.write(prompt)
    with st.chat_message("ai"):
        st.write("Here is your answer")
        st.line_chart(np.random.randn(30, 3))
        # st.write_stream(stream_data(text))
