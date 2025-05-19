# Product Feedback Site

This is a web application built with Flask that allows users to submit product feedback and upload files (Excel, Word, PDF). The app uses Google Gemini (Generative AI) to generate actionable insights based on the feedback and uploaded content.

## Features
- Submit text feedback
- Upload multiple files (.xlsx, .xls, .pdf, .docx)
- Get AI-generated actionable insights using Gemini

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd product_feedback_site
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed.
```
pip3 install -r requirements.txt
```

### 3. Set Up Google Gemini API Key
- Go to [Google AI Studio](https://makersuite.google.com/app/apikey) and generate an API key.
- Create a `.env` file in the project root and add your key:
  ```
  GOOGLE_API_KEY=your_google_api_key_here
  ```

### 4. Run the Application
```
python3 app.py
```
The app will be available at [http://localhost:5000](http://localhost:5000)

## Usage
1. Open the app in your browser.
2. Enter your feedback and upload files as needed.
3. Click Submit to receive AI-generated insights.

## Troubleshooting
- **ModuleNotFoundError:** Run `pip3 install google-generativeai` if you see `No module named 'google'`.
- **API Key Errors:** Ensure your `.env` file is present and contains a valid `GOOGLE_API_KEY`.
- **Port in Use:** If you see `OSError: [Errno 48] Address already in use`, stop other Flask servers or use a different port.

