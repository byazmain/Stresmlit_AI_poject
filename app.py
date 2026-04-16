import streamlit as st
from api_calling import note_generate
from api_calling import audio_generator
from api_calling import quiz_generator
from PIL import Image
import io
from gtts import gTTS


st.title("Note Summary and Quiz Generator",anchor=False)
st.subheader("Upload upto 3 images to generate Note and Summary")
st.divider()


with st.sidebar:
    st.subheader("Controls")
    images = st.file_uploader("Upload the photos of your notes",
                              type=['jpg','png','jpeg'],
                              accept_multiple_files=True)
    
    if images:
        if len(images)>3:
            st.error("Max you can upload 3 images.")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))
            for i,image in enumerate(images):
                with col[i]:
                    st.image(image)
    
    level = st.selectbox("Enter the difficulty of your quiz : ",
                         ("Easy","Medium","Hard"),
                         index=None)
    
    
    pressed = st.button("Click the button to initiate the AI",type="primary")
if pressed:
    if not images: 
        st.error("You must upload at least one photo.")
    if not level:
        st.error("You must select difficulty.") 
    if images and level :
        with st.container(border=2):
            st.subheader("Your Note")
            pil_image = []
            for img in images:
                pil_image.append(Image.open(img))
            with st.spinner("AI is writting for you..."):
                generated_notes = note_generate(pil_image)
                st.write(generated_notes)
            st.subheader("Audio Transcription")
            with st.spinner("AI is transcribing for you..."):
                speech = audio_generator(generated_notes)
                st.audio(speech)

        with st.container(border=2):
            with  st.spinner("AI is thinking..."):
                st.subheader(f"Quiz ({level}) Difficulty")
                quizes = quiz_generator(pil_image,level)
                st.write(quizes)

        




        
                    
