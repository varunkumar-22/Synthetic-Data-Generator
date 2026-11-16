import random
import uuid
import math
import statistics
import datetime

from structured_data_generator.templates.base import fake

EDU_STUDENT_TEMPLATE = {
    "Template Name": "EducationStudentPerformanceTemplate",

    "Subcategories": {

        # 1. Student Profile
        "Student Profile": {
            "Student Id": lambda: str(uuid.uuid4()),
            "Full Name": lambda: fake.name(),
            "Age": lambda: random.randint(12, 25),
            "Gender": lambda: random.choice(["Male", "Female", "Other"]),
            "Grade Level": lambda: random.choice([
                "6th", "7th", "8th", "9th", "10th",
                "11th", "12th", "Undergraduate", "Postgraduate"
            ])
        },

        # 2. Academic Scores
        "Academic Scores": {
            "Math Score": lambda: random.randint(0, 100),
            "Science Score": lambda: random.randint(0, 100),
            "English Score": lambda: random.randint(0, 100),
            "SocialScience Score": lambda: random.randint(0, 100),
            "Computer Score": lambda: random.randint(0, 100),
            "Overall Percentage": lambda: round(random.uniform(40, 100), 2),
            "Average Score": lambda: round(statistics.mean([random.randint(0, 100) for _ in range(5)]), 2)
        },

        # 3. Attendance
        "Attendance": {
            "Total Classes": lambda: random.randint(150, 250),
            "Classes Attended": lambda: random.randint(100, 240),
            "Attendance Percentage": lambda total, attended: round(attended / total * 100, 2)
        },

        # 4. Behavior Activity
        "Behavior Activity": {
            "Disciplinary Actions": lambda: random.randint(0, 3),
            "Participation In Events": lambda: random.choice(["Sports", "Debate", "ScienceClub", "Music", "None"]),
            "Sports Score": lambda: random.randint(0, 50),
            "Creativity Score": lambda: random.randint(0, 50),
            "Activity Index": lambda: round(statistics.mean([random.randint(0, 50), random.randint(0, 50)]), 2)
        },

        # 5. Performance Metrics
        "Performance Metrics": {
            "StudyHoursPerWeek": lambda: random.randint(2, 40),
            "HomeworkCompletionRate": lambda: random.randint(50, 100),
            "ClassParticipationScore": lambda: random.randint(1, 10),
            "Project Grade": lambda: random.choice(["A", "B", "C", "D"]),
            "Efficiency Score": lambda: round(math.sqrt(random.uniform(1, 100)) * 10, 2)
        },

        # 6. Timestamp Info
        "Timestamp Info": {
            "RecordCreatedAt": lambda: datetime.datetime.now().isoformat(),
            "LastUpdatedAt": lambda: datetime.datetime.now().isoformat(),
            "DaysSinceCreation": lambda: 0
        }
    }
}
