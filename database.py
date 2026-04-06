import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS invoices;

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    date_of_birth DATE,
    gender TEXT,
    city TEXT,
    registered_date DATE
);

CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    department TEXT,
    phone TEXT
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date DATETIME,
    status TEXT,
    notes TEXT
);

CREATE TABLE treatments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER,
    treatment_name TEXT,
    cost REAL,
    duration_minutes INTEGER
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    invoice_date DATE,
    total_amount REAL,
    paid_amount REAL,
    status TEXT
);
""")

# Dummy data
cities = ["Mumbai","Pune","Delhi","Bangalore","Hyderabad","Chennai","Nagpur"]
genders = ["M","F"]
statuses = ["Scheduled","Completed","Cancelled","No-Show"]
invoice_status = ["Paid","Pending","Overdue"]
specializations = ["Dermatology","Cardiology","Orthopedics","General","Pediatrics"]


for i in range(15):
    cursor.execute("INSERT INTO doctors (name,specialization,department,phone) VALUES (?,?,?,?)",
                   (f"Dr {i}", random.choice(specializations), "Dept", "9999999999"))

# Insert patients
for i in range(200):
    cursor.execute("""INSERT INTO patients 
    (first_name,last_name,email,phone,date_of_birth,gender,city,registered_date)
    VALUES (?,?,?,?,?,?,?,?)""",
    (f"Name{i}", f"Last{i}", None, None, "1995-01-01",
     random.choice(genders), random.choice(cities), "2024-01-01"))

# Insert appointments
for i in range(500):
    date = datetime.now() - timedelta(days=random.randint(0,365))
    cursor.execute("INSERT INTO appointments (patient_id,doctor_id,appointment_date,status,notes) VALUES (?,?,?,?,?)",
                   (random.randint(1,200), random.randint(1,15), date, random.choice(statuses), None))

# Insert treatments
for i in range(350):
    cursor.execute("INSERT INTO treatments (appointment_id,treatment_name,cost,duration_minutes) VALUES (?,?,?,?)",
                   (random.randint(1,500), "Treatment", random.randint(50,5000), random.randint(10,60)))

# Insert invoices
for i in range(300):
    total = random.randint(100,5000)
    paid = random.randint(0,total)
    cursor.execute("INSERT INTO invoices (patient_id,invoice_date,total_amount,paid_amount,status) VALUES (?,?,?,?,?)",
                   (random.randint(1,200), "2024-01-01", total, paid, random.choice(invoice_status)))

conn.commit()
print("Database created successfully!")
conn.close()
