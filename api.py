import json
from flask import Flask, jsonify, request
app = Flask(__name__)

employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]

next_employee_id = 4

def get_employee(id):
    """
    Return employee info if id matches that from id given, else return None
    """
    return next((employee for employee in employees if employee['id'] == id), None)

def employee_is_valid(employee):
    """
    Checks if user has given the 'name' value when making/updating a new employee"
    """
    for key in employee.keys():
        if key != 'name':
            return False
        return True

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist'}), 404
    return jsonify(employee)

@app.route('/employees', methods=['POST'])
def create_employee():
    global next_employee_id
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee['id'] = next_employee_id
    next_employee_id += 1
    employees.append(employee)

    return jsonify({ 
        "message": f"A new employee with name: {employee['name']} and id: {employee['id']} has been created" 
        }), 201


@app.route('/employees/<int:id>', methods=['PATCH'])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee.update(updated_employee)

    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    employees = [employee for employee in employees if employee['id'] != id]
    return jsonify(employee), 200

if __name__ == '__main__':
   app.run(port=5000)