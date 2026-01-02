import os
import io
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
import PyPDF2
import re
app = Flask(__name__, template_folder="templates")
CORS(app)

# Ensure you have your API key set correctly
client = genai.Client(api_key="YOUR API_KEY")

# ==============================
# PDF PARSING
# ==============================
def extract_text_from_pdf(file_stream):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    except Exception as e:
        print(f"Error parsing PDF: {e}")
    return text

# ==============================
# ROUTES
# ==============================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "Resume PDF is required"}), 400

    resume_file = request.files["resume"]
    resume_text = extract_text_from_pdf(io.BytesIO(resume_file.read()))
    if not resume_text.strip():
        return jsonify({"error": "Could not extract text from the PDF. Please ensure it's a text-based PDF."}), 400
    prompt = f"""
    You are a professional Resume Strategist and ATS Specialist. 
    Analyze the following resume and provide a direct evaluation. 
    Do not use fluff. Be direct and user-interactive.
    
    RESUME CONTENT:
    {resume_text}
    
    Return your response using ONLY the following structure in Markdown:
    
    # Final Resume Score: [Number]%
    
    ## 🚀 Critical Suggestions for Improvement
    Provide 3-5 high-impact, actionable bullet points using bold text for key terms. Focus on:
    - Quantifiable achievements (metrics).
    - ATS-friendly formatting fixes.
    - Missing high-demand skills based on the content.
    
    ## 💡 Pro-Tips
    A short, punchy sentence on how to make this resume stand out to recruiters.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        score_match = re.search(r"(\d+)%", response.text)
        if not score_match:
            score_match = re.search(r"Score:\s*(\d+)", response.text)
            
        score = int(score_match.group(1)) if score_match else 70

        return jsonify({
            "status": "success",
            "score": score,
            "analysis": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)
