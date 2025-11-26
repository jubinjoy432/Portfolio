from flask import Flask, render_template

app = Flask(__name__)

# Resume Data
portfolio_data = {
    "name": "Jubin Joy",
    "title": "MCA Student",
    "email": "jubinjoy432@gmail.com",
    "phone": "+91-6282353897",
    "linkedin": "https://www.linkedin.com/in/jubin-joy-658468114/",
    "github": "https://github.com/jubinjoy432",
    "summary": "Motivated MCA student with a solid foundation in computer applications and a passion for technology. Skilled in programming, web development, and problem-solving, with strong communication and teamwork abilities. Eager to learn, adapt, and contribute effectively in dynamic professional environments.",
    "experience": [
        {
            "company": "Deloitte USI",
            "role": "Associate Analyst, FinOps - Cash Application Team",
            "duration": "December 2023 - April 2025",
            "logo": "deloitte_updated.png",
            "description": [
                "Processed cash applications and managed financial transactions using Oracle.",
                "Supported FinOps operations, contributing to accurate financial data processing."
            ]
        }
    ],
    "education": [
        {
            "degree": "Master of Computer Applications (MCA)",
            "institution": "Rajagiri College Of Social Sciences, Kalamassery",
            "year": "2025 - 2027",
            "details": ""
        },
        {
            "degree": "Bachelor of Computer Application (BCA)",
            "institution": "MG University, BVM Holy Cross College, Cherpunkal",
            "year": "2020 - 2023",
            "details": "CGPA: 9.27"
        },
        {
            "degree": "Higher Secondary (CBSE)",
            "institution": "Chavara CMI Public School, Pala",
            "year": "2020",
            "details": "95.4%"
        },
        {
            "degree": "10th Grade (CBSE)",
            "institution": "Chavara CMI Public School, Pala",
            "year": "2018",
            "details": "86%"
        }
    ],
    "skills": {
        "technical": ["C", "C++", "Java", "Python", "PHP", "HTML/CSS", "JavaScript", "Web Designing", "SQL", "GIT", "Oracle"],
        "soft": ["Adaptability", "Teamwork", "Creative Thinking", "Problem Solving", "Communication"]
    },
    "certifications": [
        "RESPONSIVE WEB DESIGN Certification (FreeCodeCamp)",
        "INTRODUCTION TO CYBERSECURITY (CISCO Networking Academy)",
        "WEB DEVELOPMENT WORKSHOP Participation Certificate (IEDC, SJCET PALAI)",
        "PROGRAMMING IN PYTHON BY META (Coursera)"
    ],
    "achievements": [
        "Best Outgoing Student of The Department of Computer Science 2020-23, BVM HolyCross College, Cherpunkal, Pala",
        "8th Rank in BCA at MG University 2020-2023 (All Kerala Rank)",
        "1st Prize in Power Point Presentation - Higher Secondary School Cultural Fest, Chavara CMI Public School, Pala"
    ],
    "languages": ["Malayalam (Native)", "English (Proficient)", "Hindi (Conversational)"],
    "projects": [
        {
            "title": "Techne Events",
            "description": "A website for my college Technical Fest, serving as a central hub for event details and registration.",
            "link": "https://jubinjoy432.github.io/Techne-Events/",
            "github": "https://github.com/jubinjoy432/Techne-Events",
            "image": "techne_preview.png"
        }
    ]
}

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)



if __name__ == '__main__':
    app.run(debug=True)
