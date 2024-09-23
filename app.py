from flask import Flask, request, render_template, redirect, url_for
import openai
import pandas as pd
from docx import Document
import PyPDF2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if openai.api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

app = Flask(__name__)

# Folder where uploaded files will be saved
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Function to process Excel files
def process_excel(file_path):
    df = pd.read_excel(file_path)
    return df.describe()  # Example: summarize the data

# Function to process Word files
def process_word(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to process PDF files
def process_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to get insights using OpenAI
def get_insights(feedback, file_content):
    prompt = f"User feedback: {feedback}\nFile content: {file_content}\nProvide actionable product optimizations based on the above."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

# Route to handle file uploads and feedback processing
@app.route('/upload', methods=['POST'])
def upload_file():
    feedback = request.form['feedback']
    files = request.files.getlist('files')

    all_file_content = ""
    
    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Process each file based on its type
        if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
            result = process_excel(file_path)
        elif file.filename.endswith('.docx'):
            result = process_word(file_path)
        elif file.filename.endswith('.pdf'):
            result = process_pdf(file_path)
        
        all_file_content += str(result)
    
    # Get actionable insights using OpenAI
    insights = get_insights(feedback, all_file_content)
    
    # Return the generated insights as a response
    return f"<h2>Actionable Insights:</h2><p>{insights}</p>"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
