# 🎥 YouTube Summarizer using LLM (Gemini)

This is a simple **LLM-based YouTube Summarizer** project using Google's **Gemini-1.5-Flash** model. The app fetches YouTube transcripts and summarizes them using the LLM, presented via a **Streamlit** interface.

> ⚠️ Note: You must run this project **locally** because YouTube may block requests originating from cloud servers.

---

## 🚀 Features

- Summarizes YouTube videos using state-of-the-art LLM
- Uses Google Gemini model via API
- Streamlit-based interactive web interface
- Easily configurable with `.env` variables

---

## 🛠️ Setup Instructions

Follow these steps to get the project up and running on your local system:

1. Clone the repo or create a new project folder in your local system using your preferred IDE or code editor.

2. Open the terminal in the project directory and create a virtual environment:

   ```bash
   python -m venv venv
   ```
   it will create virtual environmental files in your project folder.

3. Create a `.env` file in the root directory to store environment variables like your **Google API Key**.

   - Get your API key from [Google AI Studio](https://makersuite.google.com/app).
   - Add this line to your `.env` file:

     ```
     GOOGLE_API_KEY="your_google_api_key_here"
     ```

4. Create a `requirements.txt` file and include all required packages. Example:

   ```txt
    youtube_transcript_api
    streamlit
    google-generativeai
    python-dotenv
    pathlib
   ```

5. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

6. Install all dependencies:

   ```bash
   pip install -r requirements.txt
   ```

7. Create your main Python file (e.g., `app.py`) and copy the main code into it.

   - Before running, make sure to:
     - Load environment variables correctly using `dotenv`.
     - Set your preferred Google model.
     - Customize the HTML/CSS/Streamlit UI as needed.

8. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Info

This project uses `gemini-1.5-flash` (or other Gemini variants) to generate the summary. You can choose an appropriate model from [Google's Gemini Models Documentation](https://ai.google.dev/).

---

## 📂 Directory Structure (Example)

```
youtube-summarizer/
│
├── .env
├── app.py
├── requirements.txt
└── venv/
```

---

## 🔐 Important Notes

- **Do NOT upload your `.env` file to GitHub.** Add it to your `.gitignore`.
- **Always test locally**, as some YouTube endpoints block cloud-based IP addresses.
- **Use your own API quota wisely**, as summarizing long transcripts can consume tokens quickly.
- **The prompt already given in the code and it limited to 250 words.**
---

## 📜 License

MIT License. Feel free to use and modify for educational or personal projects.
---

## 🙌 Acknowledgements

- [Google AI](https://ai.google.dev/) for the Gemini model
- [Streamlit](https://streamlit.io/) for the UI framework
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) for fetching transcripts
- [Edureka](https://www.youtube.com/watch?v=y1zbigWqwSQ) for project overview
---

## 📬 Suggestions or Contributions?

Feel free to open an issue or pull request if you have ideas or improvements! Happy coding 🚀
