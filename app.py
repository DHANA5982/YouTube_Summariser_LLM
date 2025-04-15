import streamlit as st
from dotenv import load_dotenv
load_dotenv()
 
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """ please summarize the following transcript of a youtube video.
Transcript it into 250 words or less and highlight the key points."""

# Funciton to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item['text'] for item in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None
    
# Function to generate a summary using google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt+transcript_text)
    return response.text

# Add a text input box for the user to enter the YouTube link
youtube_link = st.text_input("Enter the YouTube video link:")

# Button to fetch and display the detailed notes
if st.button('Get Detailed Notes'):
    if youtube_link:  # Check if the user has entered a link
        transctipt_text = extract_transcript_details(youtube_link)
        if transctipt_text:
            summary = generate_gemini_content(transctipt_text, prompt)
            st.markdown("Detailed Notes:")
            st.write(summary)
    else:
        st.error("Please enter a valid YouTube link.")
