from flask import Flask, render_template_string, request

app = Flask(__name__)

jobs = [
    {"title": "Python Developer", "company": "Tech Solutions", "location": "Hyderabad", "skills": "Python, Flask"},
    {"title": "Frontend Developer", "company": "Web Works", "location": "Remote", "skills": "HTML, CSS, JavaScript"},
    {"title": "AI Intern", "company": "AI Labs", "location": "Bangalore", "skills": "Python, AI, ML"},
]

@app.route("/")
def home():
    search = request.args.get("search", "").lower()
    filtered = [j for j in jobs if search in j["title"].lower() or search in j["skills"].lower()] if search else jobs
    html = """
    <h1>AI Job Portal</h1>
    <form><input name="search" placeholder="Search Python, AI..."><button>Search</button></form>
    {% for job in jobs %}
    <div style="border:1px solid #ddd; padding:10px; margin:10px;">
    <h3>{{ job.title }} - {{ job.company }}</h3>
    <p>{{ job.location }} | Skills: {{ job.skills }}</p>
    <button>Apply in 1-Click</button>
    </div>
    {% endfor %}
    """
    return render_template_string(html, jobs=filtered)

if __name__ == "__main__":
    app.run(debug=True)
