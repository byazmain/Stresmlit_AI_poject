import streamlit as st
import os,io
from dotenv import load_dotenv
from google import genai
from gtts import gTTS
from PIL import Image


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY25")
client = genai.Client(api_key=api_key)


def note_generate(images):
    prompt = """Summarize the picture in note format 
        at max 100 words ,make sure to add necessary markdown 
        to differentiate different section"""
    pil_img = []
    for img in images:
        pil_img.append(Image.open(img))
    response = client.models.generate_content(
        model = "gemini-flash-lite-latest", 
        contents = [pil_img,prompt]
        )
    return (response.text) 

def audio_generator(text):
    text = text.replace("#","")
    text = text.replace("*","")
    text = text.replace("'","")
    speech = gTTS(text,lang='bn',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image,difficulty):
    prompt = f"Generate only 3 quizes based on the {difficulty} level with 4 options in 4 seperate line and no extra description.Make sure to add markdown to differentiate different section with answers at last."
    pil_img = []
    for img in image:
        pil_img.append(Image.open(img))
    response = client.models.generate_content(
        model = "gemini-flash-lite-latest", 
        contents = [pil_img,prompt]
        )
    return (response.text) 
