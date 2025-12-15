from datetime import datetime

# Generate EMP table with expanded schema
emp_data = []
jobs = ['CLERK', 'SALESMAN', 'MANAGER', 'ANALYST', 'PRESIDENT']
mgr_ids = list(range(1, 21))  # Assume first 20 can be managers
deptnos = list(range(10, 80, 10)) + list(range(100, 120))  # 7 from original + 20 additional

for i in range(1, 101):
    empno = i
    ename = fake.first_name().upper()
    job = random.choice(jobs)
    mgr = random.choice(mgr_ids) if empno not in mgr_ids else None  # Avoid self as manager
    hiredate = fake.date_between(start_date='-15y', end_date='today')
    sal = random.randint(2000, 10000)
    comm = random.choice([None, round(random.uniform(100.0, 1000.0), 2)])
    deptno = random.choice(deptnos)
    
    emp_data.append([empno, ename, job, mgr, hiredate, sal, comm, deptno])

emp_df = pd.DataFrame(emp_data, columns=[
    'EmpNo', 'EName', 'Job', 'Mgr', 'HireDate', 'Sal', 'Comm', 'DeptNo'
])

# Save as CSV and SQL
emp_csv_path = "/mnt/data/emp_full_table.csv"
emp_df.to_csv(emp_csv_path, index=False)

# Generate SQL insert statements
emp_sql_lines = []
for _, row in emp_df.iterrows():
    values = (
        row.EmpNo,
        f"'{row.EName}'",
        f"'{row.Job}'",
        "NULL" if pd.isna(row.Mgr) else int(row.Mgr),
        f"'{row.HireDate}'",
        row.Sal,
        "NULL" if pd.isna(row.Comm) else row.Comm,
        row.DeptNo
    )
    sql = f"INSERT INTO Emp (EmpNo, EName, Job, Mgr, HireDate, Sal, Comm, DeptNo) VALUES ({', '.join(map(str, values))});"
    emp_sql_lines.append(sql)

emp_sql_path = "/mnt/data/emp_full_insert_statements.sql"
with open(emp_sql_path, "w") as f:
    f.write("\n".join(emp_sql_lines))

emp_csv_path, emp_sql_path
