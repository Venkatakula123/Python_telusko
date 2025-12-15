import random
import csv
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

def generate_customer_data(num_records=500000):
    data = []
    for i in range(1, num_records + 1):
        salutation = random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Prof.'])
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(['M', 'F'])
        marital_status = random.choice(['S', 'M', 'D', 'W'])  # Single, Married, Divorced, Widowed
        day_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=85)
        birth_country = fake.country()
        email_address = fake.email()
        city_name = fake.city()
        zip_code = fake.postcode()[:10]
        country_name = fake.country()
        gmt_offset = round(random.uniform(-12.0, 14.0), 2)
        preferred_cust_flag = random.choice([True, False])
        registration_time = fake.date_time_between(start_date='-5y', end_date='now')

        record = {
            "customer_pk": i,
            "salutation": salutation,
            "first_name": first_name[:20],
            "last_name": last_name[:30],
            "gender": gender,
            "marital_status": marital_status,
            "day_of_birth": day_of_birth.strftime('%Y-%m-%d'),
            "birth_country": birth_country[:60],
            "email_address": email_address[:50],
            "city_name": city_name[:60],
            "zip_code": zip_code,
            "country_name": country_name[:20],
            "gmt_timezone_offset": gmt_offset,
            "preferred_cust_flag": preferred_cust_flag,
            "registration_time": registration_time.isoformat()
        }
        data.append(record)
    return data

# Save to CSV
def save_to_csv(data, filename='customer_datal.csv.gz'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Generate and save
customer_data = generate_customer_data()
save_to_csv(customer_data)
print("✅ 500,000 customer records generated and saved to 'customer_datal.csv.gz'")