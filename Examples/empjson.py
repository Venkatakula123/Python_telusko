import random
import json

# Sample data pools
first_names = ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Kiran', 'Meera', 'Vikram', 'Anjali']
last_names = ['Sharma', 'Patel', 'Reddy', 'Verma', 'Iyer', 'Khan', 'Singh', 'Joshi']
designations = ['Software Engineer', 'Data Analyst', 'Project Manager', 'HR Executive', 'DevOps Engineer']
country = ['INDIA', 'JAPAN', 'UK', 'USA', 'CANADA', 'AFG', 'SL', 'CHINA']
salutation = ['Mr','Sri','Ms','Mrs','Miss','Srimathi','Orai']

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
        salu = random.choice(salutation)
        emp = {
            'emp_id': start_id + i,
            'salutation' : salu,
            'First_name': first,
            'Last_name': last,
            'email': email,
            'designation': designation,
            'contact_number': contact,
            'country': countrys
        }
        employees.append(emp)
    return employees

# Generate 20,000 employee records
employee_list = generate_employee_data(40)

# Save to JSON
with open('employee_data_30.json', mode='w') as file:
    json.dump(employee_list, file, indent=4)

print("✅ Successfully generated and saved 20,000 employee records to 'employee_data_30.json'")