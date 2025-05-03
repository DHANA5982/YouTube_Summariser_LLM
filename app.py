import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import re 
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

if "youtube_link" not in st.session_state:
    st.session_state["youtube_link"] = ""

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a header with a logo
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' 
             alt='YouTube Logo' width='100'>
    </div>
    """,
    unsafe_allow_html=True
)


# title of the App and Prompt for YouTube link
st.markdown("<h1 style='text-align: center;'>YouTube Video Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Enter YouTube Video Link Below</h3>", unsafe_allow_html=True)
youtube_link = st.text_input("")

# # Display YouTube thambnail if a valid link is provided
# if youtube_link:
#     try:
#         video_id = youtube_link.split("=")[1]
#         st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
#     except Exception as e:
#         st.error(f"Error fetching transcript: {e}")

prompt = """ You're a YouTube video summariser. You will taking the transcript text 
and summarizing the entire video and providing the important summary in points
within 250 words and highlight the key points. Please provide the summmary of the 
text given here. """

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

# Button to fetch and display the detailed notes
if st.button('Get Detailed Notes'):
    transctipt_text = extract_transcript_details(youtube_link)
    if transctipt_text:
        summary = generate_gemini_content(transctipt_text, prompt)
        st.markdown("Detailed Notes:")
        st.write(summary)
    else:
        st.error("Please enter a valid YouTube link.")
    
# Add a "Clear" button to reset the page
if st.button('Clear'):
    # Clear the session state or reset the input
    st.session_state["youtube_link"] = ""
    st.query_params()

footer = """
<div class="footer">
    Thanks for using this summarizer!<br>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)