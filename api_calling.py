import streamlit as st
import os,io
from dotenv import load_dotenv
from google import genai
from gtts import gTTS


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = """Summarize the picture in note format 
        at max 100 words ,make sure to add necessary markdown 
        to differentiate different section"""
def note_generate(images):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = [images,prompt]
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
    prompt =f"Generate only 3 quizes based on the {difficulty} level with 4 options and no extra description.Make sure to add markdown to differentiate different section with answer."
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = [image,prompt]
        )
    return (response.text) 
