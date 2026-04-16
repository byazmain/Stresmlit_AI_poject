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
    prompt = f"From the uploaded images, generate exactly 3 quiz questions based only on the images of {difficulty} level. Each question must have 4 multiple-choice options labeled (A), (B), (C), and (D). After listing all 3 questions, provide the correct answers in a separate section titled 'Answers' with the format: 1-?, 2-?, 3-?. Do not include any explanations, descriptions, or extra text. Only output the questions and the answers."
    response = client.models.generate_content(
        model = "gemini-3-flash-preview", 
        contents = [image,prompt]
        )
    return (response.text) 
