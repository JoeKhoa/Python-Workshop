"""
Python for Work — Beginner Seminar for CDU Students
Mapped to the PowerPoint slides and Jupyter Notebook.

Run in terminal:
    py python_for_work_beginner_seminar_mapped_final.py
"""

# ============================================================
# Slide 07 — Install packages
# ============================================================
# In terminal, install the learning packages once:
# py -m pip install notebook pandas matplotlib

# ============================================================
# Slide 11 — First Python program
# ============================================================
print("Hello, CDU!")
student_name = "Maya Chen"
print("Welcome", student_name)

# # ============================================================
# # Slide 12 — Variables and data types
# # ============================================================
# student_name = "Maya Chen"                 # str
# student_age = 22                           # int
# hours_studied = 6.5                        # float
# is_cdu_student = True                      # bool
# weekly_scores = [80, 90, 75]               # list
# campus = ("Darwin", "NT")                 # tuple
# profile = {"name": student_name, "score": 90}  # dict
# tags = {"Python", "Data", "AI"}           # set

# print(type(student_name))
# print(type(student_age))
# print(type(hours_studied))
# print(type(is_cdu_student))
# print(type(weekly_scores))
# print(type(campus))
# print(type(profile))
# print(type(tags))

# # ============================================================
# # Slide 13 — Working with strings
# # ============================================================
# student_name = "maya chen"
# course_name = "Python for Work"

# print(student_name.upper())
# print(student_name.title())
# print(len(student_name))

# message = f"Welcome {student_name.title()} to {course_name}"
# print(message)

# # ============================================================
# # Slide 14 — Working with numbers
# # ============================================================
# lab_hours = 6
# assistant_rate = 32.5
# pay = lab_hours * assistant_rate

# print(pay)
# print(round(pay, 2))

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(2 ** 3)

# # ============================================================
# # Slide 15 — Boolean logic and comparisons
# # ============================================================
# score = 72
# attendance = 0.85

# print(score > 50)
# print(score == 72)
# print(score != 100)

# can_pass = score >= 50 and attendance >= 0.8
# needs_support = score < 50 or attendance < 0.8

# print("Can pass:", can_pass)
# print("Needs support:", needs_support)

# # ============================================================
# # Slide 16 — If statements
# # ============================================================
# score = 72

# if score >= 85:
#     print("Excellent progress")
# elif score >= 50:
#     print("Pass — keep practising")
# else:
#     print("Review needed")

# # ============================================================
# # Slide 18 — Lists and tuples
# # ============================================================
# scores = [80, 90, 75]
# print(scores[0])

# scores.append(88)
# print(scores)

# location = ("Darwin", "NT")
# city, state = location
# print(city, state)

# # ============================================================
# # Slide 19 — Dictionaries and sets
# # ============================================================
# student = {
#     "name": "Maya",
#     "degree": "Engineering",
#     "score": 90
# }

# print(student["name"])
# student["score"] = 95
# print(student)

# interests = ["AI", "Data", "AI", "Business"]
# unique_interests = set(interests)
# print(unique_interests)

# # ============================================================
# # Slide 20 — For loops
# # ============================================================
# scores = [80, 90, 75]

# for score in scores:
#     print("Score:", score)

# for score in scores:
#     if score >= 50:
#         print(score, "Pass")
#     else:
#         print(score, "Review")

# # ============================================================
# # Slide 21 — Loop iterable with list and dictionary
# # ============================================================
# tasks = ["install Python", "run notebook", "write first loop"]

# for task in tasks:
#     print("Next task:", task)

# student = {"name": "Maya", "score": 90, "degree": "Engineering"}

# for key, value in student.items():
#     print(key, "=", value)

# # ============================================================
# # Slide 22 — While loop
# # ============================================================
# practice_day = 1

# while practice_day <= 5:
#     print("Practice day", practice_day)
#     practice_day = practice_day + 1

# print("Practice streak complete")

# # ============================================================
# # Slide 23 — Functions
# # ============================================================
# def calculate_pay(hours, rate):
#     pay = hours * rate
#     return pay


# def label_score(score):
#     if score >= 85:
#         return "Excellent"
#     elif score >= 50:
#         return "Pass"
#     else:
#         return "Review"

# print(calculate_pay(6, 32.5))
# print(label_score(72))

# # ============================================================
# # Slide 25 — Small data workflow
# # ============================================================
# import pandas as pd
# import matplotlib.pyplot as plt

# records = [
#     {"name": "Maya", "score": 90},
#     {"name": "Leo", "score": 72},
#     {"name": "Ava", "score": 48}
# ]

# df = pd.DataFrame(records)
# print(df)
# print(df["score"].mean())

# # ============================================================
# # Slide 26 — Final mini-project 1: create a CSV report
# # ============================================================
# students = [
#     {"name": "Maya", "score": 85},
#     {"name": "Leo", "score": 62},
#     {"name": "Ava", "score": 45},
# ]


# def get_status(score):
#     if score >= 50:
#         return "Pass"
#     else:
#         return "Review"


# for student in students:
#     student["status"] = get_status(student["score"])

# student_df = pd.DataFrame(students)
# student_df.to_csv("student_scores.csv", index=False)

# print(student_df)
# print("Average:", student_df["score"].mean())

# student_df.plot(x="name", y="score", kind="bar")
# plt.title("Student Score Report")
# plt.tight_layout()
# plt.savefig("student_score_report.png")
# plt.show()

# # ============================================================
# # Slide 27 — Final mini-project 2: read, process and visualise
# # ============================================================
# df = pd.read_csv("student_scores.csv")

# print(df.head())
# print(df["status"].value_counts())

# average_score = df["score"].mean()
# highest_score = df["score"].max()

# print("Average:", average_score)
# print("Highest:", highest_score)

# passed_students = df[df["status"] == "Pass"]
# print(passed_students)

# df.plot(x="name", y="score", kind="bar")
# plt.axhline(y=50, linestyle="--")
# plt.title("Pass Line and Student Scores")
# plt.xlabel("Student")
# plt.ylabel("Score")
# plt.tight_layout()
# plt.savefig("student_pass_line_report.png")
# plt.show()

# # ============================================================
# # Slide 28 — What to learn next
# # ============================================================
# print("Next: OOP, Python style, coding mindset and reading real Python code.")
