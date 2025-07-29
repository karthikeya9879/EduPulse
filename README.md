
# EduPulse: Bridging the Feedback Gap in Education
A secure, anonymous, and AI-powered platform for students to provide constructive feedback to professors, fostering continuous improvement in learning.

#1 The Problem
In traditional educational settings, a significant communication gap often exists between students and professors. Students frequently lack a comfortable, anonymous, and effective channel to provide constructive feedback on course content, teaching methods, or overall classroom experience. This leads to missed opportunities for pedagogical improvement, student dissatisfaction, and a potential disconnect between the learning experience and student needs. Professors, despite their dedication, may not have readily accessible, organized, and actionable insights to enhance their teaching methods.

-----------------------------------------------------------------------------------

#2 Our Solution

Edu Pulse is designed to bridge this critical feedback gap. It provides a simple, secure, and anonymous platform where students can seamlessly submit course-specific feedback. For professors, EduPulse transforms raw comments into organized, actionable insights, leveraging AI to summarize feedback constructively while intelligently filtering out negativity. This fosters a continuous loop of improvement, empowering both students to contribute to their learning environment and professors to refine their teaching strategies effectively.

-----------------------------------------------------------------------------------

#3 Key Features

* **Dual-Role Authentication:** Separate, secure login portals for Students and Professors, ensuring appropriate access control.
* **Course-Centric Feedback:** Students log in to view their enrolled courses and provide anonymous ratings and detailed comments for specific professors and subjects.
* **Professor Dashboard:** Professors access a personalized dashboard displaying:
    * Overall average rating for their courses.
    * Total number of feedback entries received.
    * (Originally: Individual feedback comments - *if you removed these, adjust this line accordingly*)
* **Intelligent AI-Powered Summarization:**
    * Professors can generate a concise, encouraging, and actionable summary of all feedback comments.
    * **Troll Filtering:** The AI is specifically prompted to disregard purely hateful, insulting, or non-constructive comments, providing a professional and positive summary.
    * **Seamless Integration:** The summary generates asynchronously, displaying smoothly without page reloads.
* **Anonymous Submissions:** Students can provide honest feedback without fear of identification.
* **Responsive & Aesthetic UI:** A clean, modern user interface designed with Tailwind CSS, featuring aesthetic fonts and subtle background animations for an engaging user experience.

------------------------------------------------------------------------------------

#4 Tech Stack

**Backend:**
* Python 3.x
* Flask (Web Framework)

**Frontend:**
* HTML5 (Structure)
* Tailwind CSS (Styling & Rapid UI Development)
* JavaScript (Client-side interactivity, especially for AI summary)
* Jinja2 (Templating Engine - integrated with Flask)

**AI Integration:**
* Google Gemini API (for feedback summarization and moderation)
* Copilot by microsoft for debugging codes

**Data Storage:**
* In-memory Python dictionaries (for hackathon prototyping purposes - data resets on server restart)

------------------------------------------------------------------------------------

#5 Getting Started

Follow these instructions to set up and run the EduPulse application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.x](https://www.python.org/downloads/) (Download the latest version)
* [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer, usually comes with Python)
* [Git](https://git-scm.com/downloads) (For cloning the repository)
* [Visual Studio Code](https://code.visualstudio.com/) (Recommended IDE)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/EduPulse.git](https://github.com/YOUR_GITHUB_USERNAME/EduPulse.git)
    cd EduPulse
    ```
2.  **Create and Activate a Virtual Environment:**
    Virtual environments help manage dependencies for your project.
    * **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
3.  **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration (Google Gemini API Key)

To enable the AI summarization feature, you need a free API key from Google AI Studio.

1.  **Get Your API Key:**
    * Visit [Google AI Studio](https://aistudio.google.com/).
    * Log in with your Google account.
    * Click "Get API key" or "Create API key" and copy the generated key.
2.  **Insert Key into `app.py`:**
    * Open the `app.py` file in your project.
    * Find the line: `API_KEY = 'YOUR_API_KEY_GOES_HERE'` line 20
    * Replace `'YOUR_API_KEY_GOES_HERE'` with your copied API key.
        ```python
        API_KEY = 'AIzaSyC...your...long...api...key...here..._w4'
        ```
    * **Save the `app.py` file.**

### Running the Application

1.  **Start the Flask Development Server:**
    Ensure your virtual environment is active in your terminal (you should see `(venv)` at the beginning of your prompt).
    ```bash
    python app.py
    ```
    You should see output indicating the server is running, typically on `http://127.0.0.1:5000`.
2.  **Access the Application:**
    Open your web browser and navigate to the address provided by Flask, usually:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

-----------------------------------------------------------------------------------

#6 Demo & Usage

Experience EduPulse by following these simple steps:

### Demo Credentials:
* **Student Login:**
    * ID: `s001`
    * Password: `pass`
* **Professor Login:**
    * ID: `p001`
    * Password: `pass`

### User Flow:

1.  **Landing Page:** Access the application and choose to login as either a `Student` or `Professor`.
    *(Optional: Add Screenshot of Landing Page)*

2.  **Student Experience:**
    * Login with student credentials.
    * You'll see your enrolled courses (e.g., Physics, Network Theory).
    * Click on a course (e.g., "Physics - Taught by Ram Kumar").
    * On the feedback form, provide a rating (1-5 stars) and a constructive anonymous comment.
    * Submit the feedback. You'll be redirected back to the student dashboard.
    *(Optional: Add Screenshot of Student Dashboard / Feedback Form)*

3.  **Professor Experience:**
    * Log out from the student session and log in as a professor (e.g., `p001 - Ram Kumar`).
    * The Professor Dashboard displays an overall average rating and total feedback received for their courses.
    * **View AI Summary:** Click the "Generate Summary" button. The AI will provide a concise, encouraging, and actionable summary of all feedback, omitting any troll comments.
    *(Optional: Add Screenshot/GIF of Professor Dashboard with AI Summary)*

*(Optional: Consider adding a short GIF demonstrating the AI summary generation process.)*

-----------------------------------------------------------------------------------

#7 Project Structure

EduPulse/
├── venv/                 # Python virtual environment (ignored by Git)
├── static/
│   └── script.js         # JavaScript for dynamic UI (e.g., AI summary loading)
├── templates/
│   ├── layout.html       # Master template for consistent UI
│   ├── landing.html      # Main landing page (student/professor login choice)
│   ├── student_login.html# Student login form
│   ├── professor_login.html# Professor login form
│   ├── student_dashboard.html# Student's view of their courses
│   ├── feedback_form.html# Form for students to submit feedback
│   └── professor_dashboard.html# Professor's view of feedback and AI summary
├── .vscode/              # VS Code specific settings (e.g., interpreter path)
├── data.py               # In-memory "database" (PROFESSORS, STUDENTS, COURSES, FEEDBACK)
├── app.py                # Flask backend application logic and routes
└── requirements.txt      # List of Python dependencies

-----------------------------------------------------------------------------------

#8 Design & Aesthetics for clean Presentation

EduPulse prioritizes a clean, intuitive, and modern user experience.

* **Tailwind CSS:** Utilized for rapid and consistent styling, ensuring a polished look across all pages.
* **Aesthetic Fonts:** Custom fonts (`Playfair Display` for headings, `Inter` for body) enhance readability and visual appeal.
* **Dynamic Background:** A subtle, animating gradient background provides a calm yet engaging visual foundation for the entire application.
* **Smooth Transitions:** CSS animations ensure seamless fade-in transitions between pages, mirroring a high-quality application feel.

-----------------------------------------------------------------------------------

#9 What's Next (Future Enhancements)

Given more time, we envision expanding EduPulse with features such as:

* **Historical Trend Analysis:** Visual charts on the professor dashboard to track average ratings over time.
* **Sentiment Breakdown:** Detailed categorization of feedback comments (e.g., Positive, Neutral, Constructive) using AI.
* **Professor Replies:** A feature for professors to post general, anonymous responses to feedback, visible to students.
* **Persistent Database:** Migrating from in-memory data to a robust database (e.g., SQLite, PostgreSQL) for permanent data storage.
* **User Management System:** Implementing more sophisticated user creation and management (e.g., admin panel).

-----------------------------------------------------------------------------------
