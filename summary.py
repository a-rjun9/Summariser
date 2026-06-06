import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

def summarise(text):
    try:
        prompt = f"Summarise the following text in 3 clear bullet points:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("=== AI Summariser (Gemini Flash) ===")
    print("Paste your text below. Press Enter twice when done:\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    
    if not text.strip():
        print("No text entered.")
        return
    
    print("\nSummarising...\n")
    print(summarise(text))

main()