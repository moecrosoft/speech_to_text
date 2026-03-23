import streamlit as st
import requests

BACKEND_URL = 'http://backend:8000'

st.title('🎧 Speech-to-Text Transcription AI')

audio = st.audio_input('Record your voice')

if audio is not None:
    st.audio(audio)  

    if st.button('Transcribe'):
        try:
            res = requests.post(
                f'{BACKEND_URL}/transcribe',
                files={'file': ('audio.wav', audio, 'audio/wav')}
            )
            st.subheader('Transcription')
            st.write(res.json()['text'])
        except Exception as e:
            st.error('Something went wrong')
            st.exception(e)

if st.button('Show History'):
    try:
        res = requests.get(f'{BACKEND_URL}/history')
        for t in res.json():
            st.write(t)
    except Exception as e:
        st.error('something went wrong')
        st.exception(e)