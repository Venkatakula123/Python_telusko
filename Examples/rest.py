from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='airahuA4360@',
    database='all_talend'
)
cursor = conn.cursor(dictionary=True)

# Endpoint to get all employees
@app.route('/emp', methods=['GET'])
def get_employees():
    cursor.execute("SELECT * FROM emp")
    result = cursor.fetchall()
    return jsonify(result)

# Endpoint to get single employee
@app.route('/emp/<int:empno>', methods=['GET'])
def get_employee(empno):
    cursor.execute("SELECT * FROM emp WHERE empno=%s", (empno,))
    result = cursor.fetchone()
    return jsonify(result) if result else ("Not found", 404)

# Endpoint to add new employee
@app.route('/emp', methods=['POST'])
def add_employee():
    data = request.json
    cursor.execute(
        "INSERT INTO emp (ename, job, sal) VALUES (%s, %s, %s)",
        (data['ename'], data['job'], data['sal'])
    )
    conn.commit()
    return jsonify({'id': cursor.lastrowid}), 201

# Endpoint to update an employee
@app.route('/emp/<int:empno>', methods=['PUT'])
def update_employee(empno):
    data = request.json
    cursor.execute(
        "UPDATE emp SET ename=%s, job=%s, sal=%s WHERE empno=%s",
        (data['ename'], data['job'], data['sal'], empno)
    )
    conn.commit()
    return ("", 204)

# Endpoint to delete an employee
@app.route('/emp/<int:empno>', methods=['DELETE'])
def delete_employee(empno):
    cursor.execute("DELETE FROM emp WHERE id=%s", (empno,))
    conn.commit()
    return ("", 204)

if __name__ == '__main__':
    app.run(debug=True)
