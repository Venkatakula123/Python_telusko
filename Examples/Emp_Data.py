import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

NUM_RECORDS = 1_000_000
DEPTNOS = list(range(10, 100))

# Define job levels and titles
JOB_LEVELS = {
    1: ['CEO'],
    2: ['CTO', 'CFO', 'COO', 'VP Engineering', 'VP Sales', 'VP HR'],
    3: ['Director', 'Principal Engineer', 'Sales Director', 'HR Director'],
    4: ['Manager', 'Team Lead', 'Project Lead'],
    5: ['Senior Engineer', 'Senior Analyst', 'Senior Sales Rep'],
    6: ['Engineer', 'Analyst', 'Sales Rep', 'HR Associate'],
    7: ['Intern', 'Trainee', 'Support Staff']
}

# Flatten job list with levels
ALL_JOBS = [(job, level) for level, jobs in JOB_LEVELS.items() for job in jobs]

# Pre-generate manager pool by level
manager_pool = {level: [] for level in JOB_LEVELS.keys()}

def generate_record(empno):
    job, level = random.choice(ALL_JOBS)
    ename = fake.first_name()[:10]
    hiredate = fake.date_between(start_date='-30y', end_date='today')
    sal = round(random.uniform(3000 + level * 1000, 20000 + level * 2000), 2)
    comm = round(random.uniform(0, 5000), 2)
    deptno = random.choice(DEPTNOS)

    # Assign manager from higher level
    mgr = None
    for higher_level in range(1, level):
        if manager_pool[higher_level]:
            mgr = random.choice(manager_pool[higher_level])
            break
    mgr = mgr if mgr else 0  # CEO has no manager

    # Add to manager pool if eligible
    if level <= 4:  # Only levels 1–4 can be managers
        manager_pool[level].append(empno)

    return [empno, ename, job, mgr, hiredate, sal, comm, deptno]

# Generate data
data = [generate_record(empno) for empno in range(1, NUM_RECORDS + 1)]
columns = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('employee_hierarchy_data3.csv', index=False)