import streamlit as st
from pipeline import generate_reels

st.set_page_config(page_title="PulsePoint AI", layout="centered")

st.title("🎯 PulsePoint AI")
st.subheader("Turn Long Talks into Viral Reels")

video = st.file_uploader("Upload Long Video", type=["mp4"])

if video:
    with open("input.mp4", "wb") as f:
        f.write(video.read())

    if st.button("🚀 Generate Reels"):
        with st.spinner("Finding emotional peaks..."):
            reels = generate_reels("input.mp4")

        st.success("Reels Generated!")

        for reel in reels:
            st.video(reel)
