# Sample-ATS
**ResuMax AI**


Your personal AI-powered resume wingman.

Applying for jobs is stressful, and the "ATS black hole" is real. I built ResuMax AI to help you see your resume through the eyes of an AI recruiter. Using Gemini 2.5 Flash, it gives you a clear score and tells you exactly what to fix to get more interviews.

🛠️ Get it Running
Setting this up is super straightforward. Just follow these steps:

Grab the essentials:

Bash: pip install flask flask-cors google-genai PyPDF2
Drop in your secret sauce: Open main.py and swap out the placeholder with your own Google AI Studio API key.


🛠️ Tech Stack: 
Component,Technology Useed: 
Frontend,"HTML5, Tailwind CSS, JavaScript (ES6+)"
Backend,"Python, Flask, Flask-CORS"
AI Model,Google GenAI (Gemini 2.5 Flash)
Parsing,PyPDF2
Icons & UI,"Lucide Icons, Marked.js (Markdown Rendering)"

Launch the engine:

Bash:python main.py
See the magic: Point your browser to http://localhost:8080.

✨ What it Does
Smart PDF Reading: No need to copy-paste. Just drop your PDF in, and the app handles the rest.

Real Talk Feedback: You won't just get a random number; you'll get 3-5 high-impact suggestions on how to improve.

Sleek Design: Built with Tailwind CSS and Lucide Icons so it's easy on the eyes and works perfectly on any screen.

💡 Pro-Tip
This was built with a Python (Flask) backend—perfect for anyone looking to see how to integrate Gemini into a real-world web app.
