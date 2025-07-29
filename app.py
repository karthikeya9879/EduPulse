import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify  
import google.generativeai as genai
import logging

# imports the data about the teachers and students based on their codes
from data import PROFESSORS, STUDENTS, COURSES, FEEDBACK

#flask application for web framework
app = Flask(__name__)
#for security purposes
app.secret_key = os.urandom(24)

#using gemini's api as it's free 
def get_ai_summary(comments):
    """
    Analyzes comments using the Gemini API and returns a constructive summary.
    """
    
    API_KEY = 'Your API KEY' 
    
    # --- Check if the API key has been set ---
    if not API_KEY or API_KEY == 'YOUR_API_KEY_GOES_HERE':
        # This is now a user-friendly message for the professor.
        return "The AI feature is not yet configured." #failsafe
    logging.error("Gemini API error", exc_info=True)
    

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Combine all comments into one block of text for the prompt
        all_feedback_text = "\n".join(f"- {c['comment']}" for c in comments)
        
        # This is the final, refined prompt suggested by copilot
        
        prompt = f"""
        You are an AI Pedagogical Coach. Your role is to provide a polite, encouraging, and insightful summary of anonymous student feedback directly to a professor.

        CRITICAL INSTRUCTIONS:
        1. TONE: Always be respectful, polite, and encouraging. Frame everything constructively.
        2. START WITH STRENGTHS: Begin your summary by highlighting the positive themes and strengths mentioned in the feedback. This is crucial for encouragement.
        3. ADDRESS AREAS FOR GROWTH: After discussing strengths, gently introduce areas for potential growth. Frame these as opportunities, not criticisms.
        4. IGNORE TROLLS: Silently disregard any comments that are purely hateful, insulting, or clearly not constructive. DO NOT mention that you have omitted any comments.
        5. FORMAT: Use bullet points for clarity. For bolding, use HTML `<b>` and `</b>` tags instead of markdown asterisks.

        Professor, here is a summary of your recent student feedback. Let's explore the insights together.

        Feedback list to analyze:
        {all_feedback_text}
        """
        
        response = model.generate_content(prompt)
        #replaces newlines with <br> tags for proper HTML rendering as suggested by copilot
        return response.text.replace('\n', '<br>')
    except Exception as e:
        print(f"An error occurred with the Gemini API: {e}")
        return "AI summary isn't available yet. Please try again later"


#Helper Function verified and debugged
def calculate_average_rating(professor_id):
    """Calculates the average rating for a given professor."""
    ratings = [f['rating'] for f in FEEDBACK.get(professor_id, [])]
    if not ratings:
        return 0
    return round(sum(ratings) / len(ratings), 1)

#Main Landing and Login Routes verified by copilot

@app.route("/")
def landing_page():
    return render_template("landing.html")

@app.route("/professor_login", methods=["GET", "POST"])
def professor_login():
    if request.method == "POST":
        professor_id = request.form.get("professor_id")
        password = request.form.get("password")
        professor = PROFESSORS.get(professor_id)
        if professor and professor["password"] == password:
            session["user_type"] = "professor"
            session["user_id"] = professor_id
            return redirect(url_for("professor_dashboard"))
        else:
            flash("Invalid Professor ID or Password.", "error")
            return redirect(url_for("professor_login"))
    return render_template("professor_login.html", professors=PROFESSORS)

@app.route("/student_login", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        password = request.form.get("password")
        student = STUDENTS.get(student_id)
        if student and student["password"] == password:
            session["user_type"] = "student"
            session["user_id"] = student_id
            return redirect(url_for("student_dashboard"))
        else:
            flash("Invalid Student ID or Password.", "error")
            return redirect(url_for("student_login"))
    return render_template("student_login.html", students=STUDENTS)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing_page"))

#  Student Dashboard and Actions 

@app.route("/student_dashboard")
def student_dashboard():
    if session.get("user_type") != "student":
        return redirect(url_for("student_login"))
    
    student_id = session["user_id"]
    student_info = STUDENTS[student_id]
    
    student_courses = []
    for course_id in student_info["enrolled_courses"]:
        course = COURSES[course_id]
        professor = PROFESSORS[course["professor_id"]]
        student_courses.append({
            "id": course_id,
            "name": course["name"],
            "professor_name": professor["name"]
        })
        
    return render_template(
        "student_dashboard.html", 
        student_name=student_info["name"],
        courses=student_courses
    )

@app.route("/give_feedback/<course_id>")
def give_feedback_page(course_id):
    if session.get("user_type") != "student":
        return redirect(url_for("student_login"))

    course = COURSES.get(course_id)
    if not course:
        flash("Course not found.", "error")
        return redirect(url_for("student_dashboard"))

    professor = PROFESSORS.get(course["professor_id"])
    
    return render_template(
        "feedback_form.html",
        course_name=course["name"],
        professor_name=professor["name"],
        course_id=course_id
    )

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    if session.get("user_type") != "student":
        return redirect(url_for("student_login"))

    course_id = request.form.get("course_id")
    rating = int(request.form.get("rating"))
    comment = request.form.get("comment")

    professor_id = COURSES[course_id]["professor_id"]

    if professor_id in FEEDBACK:
        FEEDBACK[professor_id].append({"rating": rating, "comment": comment})
    
    flash("Your feedback for " + COURSES[course_id]['name'] + " has been submitted!", "success")
    return redirect(url_for("student_dashboard"))

# Professor Dashboard and AI Route verified by copilot

@app.route("/professor_dashboard")
def professor_dashboard():
    if session.get("user_type") != "professor":
        return redirect(url_for("professor_login"))

    professor_id = session["user_id"]
    professor_info = PROFESSORS.get(professor_id)
    professor_feedback = FEEDBACK.get(professor_id, [])
    
    average_rating = calculate_average_rating(professor_id)
    total_feedback_count = len(professor_feedback)

    return render_template(
        "professor_dashboard.html",
        professor=professor_info,
        feedback_list=professor_feedback,
        average_rating=average_rating,
        total_feedback=total_feedback_count,
        professor_id=professor_id # Pass professor_id for the AI button
    )

@app.route("/summarize/<professor_id>")
def summarize(professor_id):
    """The new route that the frontend will call to get the AI summary."""
    if session.get("user_type") != "professor":
        return jsonify({"error": "Unauthorized"}), 403

    comments = FEEDBACK.get(professor_id, [])
    if not comments:
        return jsonify({"summary": "Not enough feedback to summarize."})

    summary = get_ai_summary(comments)
    return jsonify({"summary": summary})


#code execution
if __name__ == "__main__":
    app.run(debug=True)

