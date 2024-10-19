from flask import Flask, request, jsonify
from database.create_user import user_exists, create_user
import base64

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user_endpoint():
    data = request.json
    
    user_name = data.get('user_name')
    face_image = data.get('face_image')  # Expecting a base64 encoded image

    if not user_name or not face_image:
        return jsonify({"error": "User name and face image are required."}), 400

    # Check if the user already exists
    if user_exists(user_name):
        return jsonify({"error": "User already exists."}), 409

    # Decode the base64 encoded image
    face_image_blob = base64.b64decode(face_image)

    # Create a new user
    user_id = create_user(user_name, face_image_blob)

    return jsonify({"user_id": user_id, "message": "User created successfully."}), 201




if __name__ == '__main__':
    app.run(debug=True)
