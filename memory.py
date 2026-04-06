from vanna_setup import create_agent

agent, memory = create_agent()

pairs = [
    ("How many patients?", "SELECT COUNT(*) FROM patients"),
    ("List all doctors", "SELECT name, specialization FROM doctors"),
    ("Total revenue", "SELECT SUM(total_amount) FROM invoices"),
    ("Unpaid invoices", "SELECT * FROM invoices WHERE status!='Paid'"),
    ("Patients by city", "SELECT city, COUNT(*) FROM patients GROUP BY city"),
]

for q, sql in pairs:
    memory.save_correct_tool_use(q, {"sql": sql})

print("Memory seeded!")
