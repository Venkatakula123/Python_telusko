import random
import csv

# Sample data pools
first_names = ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Kiran', 'Meera', 'Vikram', 'Anjali']
last_names = ['Sharma', 'Patel', 'Reddy', 'Verma', 'Iyer', 'Khan', 'Singh', 'Joshi']
designations = ['Software Engineer', 'Data Analyst', 'Project Manager', 'HR Executive', 'DevOps Engineer']

# Function to generate employee data
def generate_employee_data(num_records, start_id=101):
    employees = []
    for i in range(num_records):
        first = random.choice(first_names)
        last = random.choice(last_names)
        email = f"{first.lower()}.{last.lower()}{start_id + i}@example.com"
        designation = random.choice(designations)
        emp = {
            'emp_id': start_id + i,
            'First_name': first,
            'Last_name': last,
            'email': email,
            'designation': designation
        }
        employees.append(emp)
    return employees

# Generate 10,000 employee records
employee_list = generate_employee_data(10000)

# Save to CSV
with open('employee_data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['emp_id', 'First_name', 'Last_name', 'email', 'designation'])
    writer.writeheader()
    writer.writerows(employee_list)

print("✅ Successfully generated and saved 10,000 employee records to 'employee_data.csv'")