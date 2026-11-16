import random
import math
import datetime

from forma.templates.base import fake

HEALTHCARE_TEMPLATE = {
    "Template Name": "healthcare_medical_template",

    "Subcategories": {

        # 1. Patient Info
        "Patient Info": {
            "Patient Id": lambda: fake.uuid4(),
            "Full Name": lambda: fake.name(),
            "Age": lambda: random.randint(1, 95),
            "Gender": lambda: random.choice(["Male", "Female", "Other"]),
            "Blood Group": lambda: random.choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]),
            "Contact Number": lambda: fake.phone_number(),
            "Email": lambda: fake.email(),
            "Address": lambda: fake.address().replace("\n", ", "),
            "Risk Score": lambda: random.randint(1, 100)
        },

        # 2. Medical Record
        "Medical Record": {
            "Record Id": lambda: fake.uuid4(),
            "Diagnosis": lambda: random.choice([
                "Hypertension", "Diabetes", "Asthma", "Migraine", "Allergy",
                "Arthritis", "Viral Infection", "Flu", "Back Pain", "Cholesterol"
            ]),
            "Symptoms": lambda: random.choice([
                "Fever, Cough, Fatigue",
                "Headache, Nausea",
                "Chest Pain, Dizziness",
                "Joint Pain, Swelling",
                "Shortness of Breath"
            ]),
            "Severity": lambda: random.choice(["Mild", "Moderate", "Severe", "Critical"]),
            "Diagnosis Date": lambda: fake.date(),
            "Severity Score": lambda: random.randint(1, 100)
        },

        # 3. Doctor Info
        "Doctor Info": {
            "Doctor Id": lambda: fake.uuid4(),
            "Doctor Name": lambda: fake.name(),
            "Specialization": lambda: random.choice([
                "General Physician", "Cardiologist", "Neurologist",
                "Dermatologist", "Pediatrician", "Orthopedic",
                "Gynecologist", "ENT Specialist"
            ]),
            "Hospital Name": lambda: random.choice([
                "Apollo Hospital", "Fortis Hospital", "AIIMS", "Max Healthcare",
                "Narayana Health", "Care Hospitals", "KIMS Hospitals"
            ]),
            "Next Available Slot": lambda: (
                datetime.datetime.now() + datetime.timedelta(
                    minutes=random.randint(15, 240)
                )
            ).isoformat()
        },

        # 4. Appointment Info
        "Appointment Info": {
            "Appointment Id": lambda: fake.uuid4(),
            "Appointment Date": lambda: fake.iso8601(),
            "Appointment Status": lambda: random.choice(["Scheduled", "Completed", "Cancelled", "No-Show"]),
            "Consultation Type": lambda: random.choice(["In-Person", "Online Video", "Telephonic"]),
            "Estimated Wait Time Min": lambda: random.randint(5, 60)
        },

        # 5. Prescription Info
        "Prescription Info": {
            "Prescription Id": lambda: fake.uuid4(),
            "Medicine Name": lambda: random.choice([
                "Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine",
                "Vitamin D", "Metformin", "Aspirin", "Omeprazole"
            ]),
            "Dosage": lambda: random.choice([
                "1 tablet daily", "2 tablets daily", "1 tablet after meals"
            ]),
            "Duration Days": lambda: random.randint(3, 30),
            "Dosage Effectiveness Score": lambda: round(
                random.uniform(0.6, 1.0) * math.sqrt(random.random()),
                3
            )
        },

        # 6. Billing Info
        "Billing Info": {
            "Invoice Id": lambda: fake.uuid4(),
            "Consultation Fee": lambda: random.randint(300, 2000),
            "Medicine Charges": lambda: random.randint(50, 5000),
            "Lab Test Charges": lambda: random.randint(100, 8000),
            "Total Bill": lambda: (
                lambda cf, mc, lt: cf + mc + lt
            )(
                random.randint(300, 2000),
                random.randint(50, 5000),
                random.randint(100, 8000)
            ),

            "Payment Method": lambda: random.choice(["Cash", "Credit Card", "UPI", "Insurance", "Wallet"]),
            "Payment Status": lambda: random.choice(["Paid", "Pending", "Failed"])
        },

        # 7. Device Info(for telemedicine)
        "Device Info": {
            "Device Type": lambda: random.choice(["Mobile", "Desktop", "Tablet"]),
            "Os": lambda: random.choice(["Android", "iOS", "Windows", "MacOS"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"]),
            "Avg Response Time Ms": lambda: random.randint(50, 300)
        }
    }
}
