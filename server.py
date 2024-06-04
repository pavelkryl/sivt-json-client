from typing import Tuple
from flask import Flask, Response, request, jsonify

app = Flask(__name__)

# Sample data
data = {
    "students": [
        {"id": 1, "jmeno": "Alice", "vek": 23, "obor": "ICT", "aktivni": True},
        {"id": 2, "jmeno": "Bob", "vek": 24, "obor": "Matematika", "aktivni": True},
        {"id": 3, "jmeno": "Charlie", "vek": 22, "obor": "Fyzika", "aktivni": False}
    ]
}

ServerReply = Tuple[Response, int]

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students() -> Response:
    return jsonify(data["students"])

# Route to get a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id: int) -> ServerReply:
    student = next((item for item in data["students"] if item["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student() -> ServerReply:
    new_student = request.get_json()
    if "id" not in new_student or "jmeno" not in new_student or "vek" not in new_student or "obor" not in new_student or "aktivni" not in new_student:
        return jsonify({"error": "Invalid student data"}), 400
    if new_student.get("id") in [s.get("id") for s in data["students"]]:
        return jsonify({ "error": f"id {new_student.get("id")} already used"}), 409
    data["students"].append(new_student)
    return jsonify(new_student), 201

# Route to update an existing student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id: int) -> ServerReply:
    updated_student = request.get_json()
    student = next((item for item in data["students"] if item["id"] == student_id), None)
    if student:
        student.update(updated_student)
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

# Route to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id: int) -> ServerReply:
    global data
    data["students"] = [item for item in data["students"] if item["id"] != student_id]
    return jsonify({"message": "Student deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
