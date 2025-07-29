#flag data for the prototype with real time feedback input

# Professor data: ID, name, and a simple password for the demo.
PROFESSORS = {
    "p001": {"name": "Ram Kumar", "password": "pass"},
    "p002": {"name": "Jayram Mohan", "password": "pass"},
    "p003": {"name": "Sivadarshini Rajalakshmi K", "password": "pass"},
    "p004": {"name": "Balaji Sampath", "password": "pass"},
    # Added a 5th professor for the 5th class as a placeholder.
    "p005": {"name": "Priya Sharma", "password": "pass"},
}

# Course data, linking a course name to a professor.
COURSES = {
    "c101": {"name": "Physics", "professor_id": "p001"},
    "c102": {"name": "Network Theory", "professor_id": "p002"},
    "c103": {"name": "Basic Engineering", "professor_id": "p003"},
    "c104": {"name": "Problem Solving using Python", "professor_id": "p004"},
    "c105": {"name": "Multivariable Calculus", "professor_id": "p005"},
}

# Student data, now including a list of enrolled course IDs.
# For the demo, all students are enrolled in all courses.
STUDENTS = {
    "s001": {"name": "Aarav", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s002": {"name": "Vivaan", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s003": {"name": "Aditya", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s004": {"name": "Vihaan", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s005": {"name": "Arjun", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s006": {"name": "Sai", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s007": {"name": "Reyansh", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s008": {"name": "Ayaan", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s009": {"name": "Krishna", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s010": {"name": "Ishaan", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s011": {"name": "Ananya", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s012": {"name": "Diya", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s013": {"name": "Saanvi", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s014": {"name": "Myra", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
    "s015": {"name": "Aadhya", "password": "pass", "enrolled_courses": ["c101", "c102", "c103", "c104", "c105"]},
}

# Feedback data, keyed by professor ID.
# This starts empty. All feedback will be added live from the website. #verified by copilot
FEEDBACK = {
    "p001": [],
    "p002": [],
    "p003": [],
    "p004": [],
    "p005": [],
}
