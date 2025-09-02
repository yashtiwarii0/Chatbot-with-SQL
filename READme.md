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
