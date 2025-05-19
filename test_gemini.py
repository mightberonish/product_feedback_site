import google.generativeai as genai

genai.configure(api_key="AIzaSyAdXnM54Kv8CWg6XYm02ce6d84cC1UYlOk")
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("Explain how AI works")
print(response.text)

def get_insights(feedback, file_content):
    prompt = f"User feedback: {feedback}\nFile content: {file_content}\nProvide actionable product optimizations based on the above."
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text