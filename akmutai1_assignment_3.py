# ==============================
# Personal Academic & Life Portfolio
# ==============================

# 1. Personal Information
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# 2. Academic Data
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list = [3, 3, 3, 3]                       
gpa_history = [3.2, 3.6, 3.4, 3.7]    

# 3. Contact Information
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)

# 4. Interest Tracking
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests_set = {"Software development", "Web development", "Data science", "Game development"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# 5. Organizational Mapping
course_credits = {
    "COMP 163": 3,
    "MATH 150": 3,
    "ENG 101": 3,
    "HIS 105": 3
}

course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}

course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}

monthly_budget = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
}

study_hours_per_subject = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}

contact_directory = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}


# ==============================
# Required Calculations
# ==============================

# a) Total current credits
total_current_credits = sum(credit_hours_list)

# b) Cumulative GPA
cumulative_gpa = round(sum(gpa_history) / len(gpa_history), 2)

# c) Completed courses count
completed_courses_count = len(completed_courses)

# d) Total weekly study hours
total_weekly_study_hours = sum(study_hours_per_subject.values())

# e) Academic load
academic_load = total_current_credits + total_weekly_study_hours

# f) Monthly budget total
monthly_budget_total = sum(monthly_budget.values())

# g) Daily food budget
daily_food_budget = round(monthly_budget["Food"] / 30, 1)

# h) Annual budget projection
annual_budget_projection = monthly_budget_total * 12

# i) Study cost per hour
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 1)

# j) Social media followers
total_social_followers = instagram_info[2] + twitter_info[2]

# ==============================
# Output Formatting
# ==============================

print("="*63)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("="*63)

# Student Info
print(f"Student: {full_name}")
print(f"Email: {student_email}")
print(f"From: {hometown}")
print(f"Graduating: {graduation_semester}")
print(f"Major: {major}")

# Academic Profile
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()
print("Current Courses:")
print(f"COMP 163 - {course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"MATH 150 - {course_credits['MATH 150']} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(f"ENG 101 - {course_credits['ENG 101']} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(f"HIS 105 - {course_credits['HIS 105']} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
print()

# Personal Development
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {len(current_skills_set)}")
print(f"Skills Want to Learn: {len(skills_to_learn_set)}")
print()

# Financial Overview
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}")
print()

# Connections & Contacts
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_social_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")
print()

# Life Statistics
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog_set)} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("="*63)
