# Chatbot-with-SQL

A simple and effective SQL chatbot built with Python, Streamlit, and SQLite—perfect for querying a student database using natural language via a friendly chat interface.

**Live Demo:** [Try it out here](https://chatbot-with-sql.streamlit.app/)

---

##  Project Overview

This project enables users to interact with a `student.db` SQLite database through an intuitive Streamlit-powered chatbot. You can submit natural language queries like *“Show all students”* and the app handles execution and display behind the scenes.

---

##  Repository Structure

Chatbot-with-SQL/
├── app.py # Core Streamlit application logic
├── sqllite.py # SQLite database handler
├── student.db # Pre-populated database (e.g., student data)
├── requirements.txt # Project dependencies
├── README.md # (This) Project documentation
└── venv/ # Virtual environment (likely should be excluded)


---

##  Getting Started

### Prerequisites

- Python 3.8+ installed
- Optional: `venv` or `virtualenv` to manage dependencies

### Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yashtiwarii0/Chatbot-with-SQL.git
   cd Chatbot-with-SQL

    Set up a virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

Install dependencies

    pip install -r requirements.txt

    Ensure student.db is present in the project root—this should contain at least one table (e.g., students) with sample data.

Running the App

Launch the chatbot interface using:

streamlit run app.py

Once running, open the local URL displayed in your terminal (usually http://localhost:8501) to interact with the chatbot.
How It Works

    User Input
    Enter a query via the Streamlit chat UI, such as:

        "List all students"

        "Find student with roll number 5"

    Backend Handling

        The text input is sent to sqllite.py, which translates or executes it as a SQL command against student.db.

        Results are fetched and returned to app.py.

    Response Presentation
    The query result is rendered neatly in the chat interface for easy reading.

Example Interactions
User Input	Expected Action
Show all students	Displays every student in database
Student with roll 5	Shows information for roll number 5
Add student John, roll 6, grade A	Inserts a new record (if supported)
Delete student with roll 3	Removes specified student (if supported)

(Adjust these examples if your implementation supports them.)
Customization & Extension Ideas

    Enhance language parsing for more conversational or flexible query formats.

    Support CRUD operations like adding, updating, or deleting records.

    Switch database backends (e.g., PostgreSQL, MySQL) for production-readiness.

    Improve UI/UX, adding query history, buttons, or inline feedback.

    Add prompt validation to safeguard against invalid or potentially destructive SQL.

Dependencies

Dependencies listed in requirements.txt typically include:

streamlit
sqlite3      # Built-in, may not need explicit installation
pandas      # If used for data handling and display

(Confirm and list exact packages from your file.)
Contributing

Contributions are welcome! You can:

    Fix bugs or typos

    Improve query parsing or UI

    Add documentation, examples, or tests

Please fork the repository, make your changes, and submit a pull request.
License

(Specify the license if there is one—like MIT or Apache—otherwise note that no license is provided.)

# 💫 About Me:
👋 Hey there, I’m Yash Tiwari<br><br>🚀 AI & Machine Learning Enthusiast | Data-Driven Problem Solver | Aspiring AI Engineer<br><br>I love building intelligent systems that transform raw data into meaningful insights and impactful solutions. With a strong foundation in Machine Learning, Deep Learning, and Data Science, I aim to bridge the gap between business strategy and cutting-edge technology.<br><br>🧑‍💻 About Me<br><br>🎓 Pursuing B.Tech in Computer Science & Business Systems (KIT’s College of Engineering, GPA 8.1).<br><br>💼 Experience as Business Development Manager, blending communication and problem-solving with technical innovation.<br><br>🔬 Hands-on with Flask, TensorFlow, PyTorch, Hugging Face, MLFlow, SQL, Docker, and NLP tools like NLTK.<br><br>📊 Passionate about deploying end-to-end ML systems, from data preprocessing → model building → deployment.<br><br>🏗️ Highlight Projects<br><br>📘 Student Performance Predictor


## 🌐 Socials:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/https://www.linkedin.com/in/yashtiwari27/) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:yashtiwaric19@gmail.com) 

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![nVIDIA](https://img.shields.io/badge/cuda-000000.svg?style=for-the-badge&logo=nVIDIA&logoColor=green) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Neo4J](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Scipy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![nVIDIA](https://img.shields.io/badge/nVIDIA-%2376B900.svg?style=for-the-badge&logo=nVIDIA&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=yashtiwarii0&theme=dark&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://nirzak-streak-stats.vercel.app/?user=yashtiwarii0&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=yashtiwarii0&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

---
[![](https://visitcount.itsvg.in/api?id=yashtiwarii0&icon=0&color=1)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->


