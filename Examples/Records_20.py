# Generate 20 more unique department records
additional_dept_data = []
locations = ['New York', 'Dallas', 'Chicago', 'Boston', 'Los Angeles', 'San Francisco', 'Seattle', 'Austin', 'Miami', 'Denver']
base_dept_no = 100  # Start from 100 to avoid conflict with earlier IDs

for i in range(20):
    dept_no = base_dept_no + i
    dept_name = f"{fake.word().capitalize()} Dept"
    location = random.choice(locations)
    additional_dept_data.append([dept_no, dept_name, location])

dept_df = pd.DataFrame(additional_dept_data, columns=['DeptNo', 'DName', 'Location'])

# Save as CSV and SQL
dept_csv_path = "C://Users//Venka//Downloads//FilesTalend//additional_dept_table.csv"
dept_df.to_csv(dept_csv_path, index=False)

# Generate SQL insert statements
insert_statements = []
for _, row in dept_df.iterrows():
    sql = f"INSERT INTO Dept (DeptNo, DName, Location) VALUES "f"({row.DeptNo}, '{row.DName.replace('\'', '\'\'')}', '{row.Location}');"
    insert_statements.append(sql)

dept_sql_path = "/mnt/data/additional_dept_insert_statements.sql"
with open(dept_sql_path, "w") as f:
    f.write("\n".join(insert_statements))

dept_csv_path, dept_sql_path