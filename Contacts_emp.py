import random
import csv

# Sample data pools
first_names = ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Kiran', 'Meera', 'Vikram', 'Anjali']
last_names = ['Sharma', 'Patel', 'Reddy', 'Verma', 'Iyer', 'Khan', 'Singh', 'Joshi']
designations = ['Software Engineer', 'Data Analyst', 'Project Manager', 'HR Executive', 'DevOps Engineer']
country = ['INDIA','JAPAN','UK','USA','CANADA','AFG','SL','CHINA']

# Function to generate random Indian mobile number
def generate_contact_number():
    return f"{random.choice(['9', '8', '7'])}{random.randint(100000000, 999999999)}"

# Function to generate employee data
def generate_employee_data(num_records, start_id=1000):
    employees = []
    for i in range(num_records):
        first = random.choice(first_names)
        last = random.choice(last_names)
        email = f"{first.lower()}.{last.lower()}{start_id + i}@example.com"
        designation = random.choice(designations)
        contact = generate_contact_number()
        countrys = random.choice(country)
        emp = {
            'emp_id': start_id + i,
            'First_name': first,
            'email': email,
            'Last_name': last,
            'country': countrys,
            'designation': designation,
            'contact_number': contact
            
        }
        employees.append(emp)
    return employees

# Generate 20,000 employee records
employee_list = generate_employee_data(20000)

# Save to CSV
with open('employee_data_50000.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['emp_id', 'First_name', 'Last_name', 'email', 'designation', 'contact_number','country'])
    writer.writeheader()
    writer.writerows(employee_list)

print("✅ Successfully generated and saved 20,000 employee records to 'employee_data_50000.csv'")