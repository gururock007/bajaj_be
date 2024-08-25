from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    input_data = data.get('data', [])

    # Extract user details (hardcoded for now)
    user_id = "Gurushik JAYAKUMAR"
    email = "gurushikjayakumar@gmail.com"
    roll_number = "21BEC1561"

    # Separate numbers and alphabets
    numbers = [item for item in input_data if item.isdigit()]
    alphabets = [item for item in input_data if item.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = [max(lowercase_alphabets, default="")] if lowercase_alphabets else []

    # Prepare response
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response), 200
@app.route('/', methods=['GET','POST'])
def index():
    return "Welcome to the BFHL API!"

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run( debug=True, port=5000, host='0.0.0.0')
